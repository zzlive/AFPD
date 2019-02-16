# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 00:37:00 2018

@author: Frankie Ho
"""
#%%
##Scraping financial data using Selenium, import packages first
import pandas as pd
import os 
from numpy import nan
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = r'D:\C Disk Transfer\Desktop\AFPD\other_packages\web_scraping'

#%%
"""
Objective: Scrape quarterly financial information (Income statement and balance sheet) of listed companies
"""

## create a pandas dataframe to store the scraped data
df = pd.DataFrame(index=range(20),
                  columns=['company', 'quarter', 'quarter_ending', 
                           'total_revenue', 'gross_profit', 'net_income', 
                           'total_assets', 'total_liabilities', 'total_equity', 
                           'net_cash_flow'])

#%% 
## launch the Chrome browser, please change directory to the location of your Chromedriver exe file and save that as my_path
#my_path = r"C:\Users\Zigan Wang\Downloads\chromedriver_win32_229\chromedriver.exe"
my_path = r'C:\Users\Zigan Wang\Downloads\IEDriverServer_x64_3.12.0\IEDriverServer.exe'
browser = webdriver.Ie(executable_path=my_path)
browser.maximize_window()

"""url format, later we substitute each curly brackets by different values to scrape different data we need
first space is ticker (aapl, etc.), second space is type of data (income statement, balance sheet, etc.)"""
url_form = "http://www.nasdaq.com/symbol/{}/financials?query={}&data=quarterly" 

"""elements (html code) that contain financial data of interest are organized in the same way. General form is given as financials_xpath below
When the curly bracket (text() = '{}') is substituted by the name of financial data (Total Assets, Total Libilities, etc.),
the complete element is generated and can be searched directly. """
#find all td (standard cells) with parent tr (row) and grandparent tbody, 
#where the th (header cell) in the same row is the name of financial data we want to scrape
financials_xpath = "//tbody/tr/th[text() = '{}']/../td[contains(text(), '$')]"

#%%
"""Quick way to check whether we access the correct page before scraping the real data. 
We should scrape stock data of Amazon, Apple, Facebook, IBM and Microsoft. 
We only scrape the page titles and put them into a list. Then we compare the list and the input tickers"""
## company ticker symbols 
symbols = ["amzn", "aapl", "fb", "ibm", "msft"]
company = []
 
for i, symbol in enumerate(symbols):
    ## navigate to income statement quarterly page of each symbol  
    url = url_form.format(symbol, "income-statement")
    browser.get(url)
  
#xpath allows us to locate elements of interest inside html code. In this case, we want to scrape page titles
#find all h1 tags (headings) in the page containing text 'Company Financials'. Results are saved in a list 'company'
#10 seconds are given to identify elements that satisfy the previous condition. If elements are not found, nan is appended to the list
    company_xpath = "//h1[contains(text(), 'Company Financials')]"
    try:
        company.append(WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, company_xpath))).text)
    except:
        company.append(nan)
        
print(company)
        
#%% 
## define a new function returns nan values if elements not found, and converts the webelements to text
def get_elements(xpath):
    elements = browser.find_elements_by_xpath(xpath) # find the elements according to conditions stated in xpath
    if len(elements) != 4: # if any are missing, return all nan values
        return [nan] * 4 
    else: # otherwise, return just the text of the element
        text = []
        for e in elements:
            text.append(e.text)
        return text

#%%
# Main function
if __name__=="__main__":
    
    """Scrape several financial variables of five stocks with a for loop and get_elements function defined above. 
    Save results in a dataframe"""       
    ## company ticker symbols, Here we have Amazon, Apple, Facebook, IBM and Microsoft
    symbols = ["amzn", "aapl", "fb", "ibm", "msft"]
    
    for i, symbol in enumerate(symbols): #"amzn"=0, "aapl"=1, etc.
        ## navigate to income statement quarterly page    
        url = url_form.format(symbol, "income-statement")
        browser.get(url)
        
        #Find page titles in h1 format (heading) with text containing "Company Financials"
        company_xpath = "//h1[contains(text(), 'Company Financials')]"
        company = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, company_xpath))).text
        
        #Find quarters by identifying th (header cells) under tr under thead, where first th item contains text "Quarter:" 
        #we scrape only the third and later th items. There should be four items
        quarters_xpath = "//thead/tr[th[1][text() = 'Quarter:']]/th[position()>=3]"
        quarters = get_elements(quarters_xpath)
        
        #Find quarters ending dates by identifying th (header cells) with parant tr (row) and grandparent thead, 
        #where first th item contains text "Quarter Ending:"
        #we scrape only the third and later th items. There should be four items
        quarter_endings_xpath = "//thead/tr[th[1][text() = 'Quarter Ending:']]/th[position()>=3]"
        quarter_endings = get_elements(quarter_endings_xpath)
        
        #Scrape total revenue, gross profit and net_income of each quarter, refer to financials_xpath format for details
        #header cell is "Total Revenue", find remaining four items in this row
        total_revenue = get_elements(financials_xpath.format("Total Revenue"))
        #header cell is "Gross Profit", find remaining four items in this row
        gross_profit = get_elements(financials_xpath.format("Gross Profit"))
        #header cell is "Net Income", find remaining four items in this row
        net_income = get_elements(financials_xpath.format("Net Income"))
        
        ## navigate to balance sheet quarterly page 
        url = url_form.format(symbol, "balance-sheet")
        browser.get(url)
        
        total_assets = get_elements(financials_xpath.format("Total Assets"))
        total_liabilities = get_elements(financials_xpath.format("Total Liabilities"))
        total_equity = get_elements(financials_xpath.format("Total Equity"))
        
        ## navigate to cash flow quarterly page 
        url = url_form.format(symbol, "cash-flow")
        browser.get(url)
        
        net_cash_flow = get_elements(financials_xpath.format("Net Cash Flow"))
        
    ## fill the datarame with the scraped data, 4 rows per company
        for j in range(4):  
            row = (i * 4) + j
            df.loc[row, 'company'] = company
            df.loc[row, 'quarter'] = quarters[j]
            df.loc[row, 'quarter_ending'] = quarter_endings[j]
            df.loc[row, 'total_revenue'] = total_revenue[j]
            df.loc[row, 'gross_profit'] = gross_profit[j]
            df.loc[row, 'net_income'] = net_income[j]
            df.loc[row, 'total_assets'] = total_assets[j]
            df.loc[row, 'total_liabilities'] = total_liabilities[j]
            df.loc[row, 'total_equity'] = total_equity[j]
            df.loc[row, 'net_cash_flow'] = net_cash_flow[j]
    
    browser.quit()
     
    ## create a csv file in our working directory with our scraped data
    df.to_csv(path + os.sep + "company financials.csv", index=False)