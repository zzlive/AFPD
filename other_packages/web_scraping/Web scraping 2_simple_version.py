# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 00:37:00 2018

@author: Frankie Ho
"""

##Scraping financial data using Selenium, import packages first
import pandas as pd
from numpy import nan
from selenium import webdriver

"""
Objective: Scrape quarterly financial information (Income statement and balance sheet) of listed companies
"""

## create a pandas dataframe to store the scraped data
# df = pd.DataFrame(index=range(20),
#                   columns=['company', 'quarter', 'quarter_ending',
#                            'total_revenue', 'gross_profit', 'net_income',
#                            'total_assets', 'total_liabilities', 'total_equity',
#                            'net_cash_flow'])

df = pd.DataFrame(index=range(20),
                  columns=['company', 'years', 'year_endings',
                           'current_ratio','quick_ratio', 'cash_ratio', 'gross_margin',
                           'operating_margin', 'pre_tex_margin', 'profit_margin',
                           'pre_tax_roe','after_tax_roe'])

## launch Firefox driver, please change directory to the location of your Geckodriver exe file and save that as my_path
#Use Chromedriver for launching chrome
#Use Edgedriver for launching edge
my_path = r"C:\Users\zzliv\Downloads\chromedriver_win32\chromedriver.exe"
browser = webdriver.Chrome(executable_path=my_path) #webdriver.Chrome for chromedriver
browser.maximize_window()

# Main function 

"""Scrape several financial variables of five stocks with a for loop and get_elements function defined above. 
Save results in a dataframe"""       
## company ticker symbols, Here we have Amazon, Apple, Facebook, IBM and Microsoft
symbols = ["amzn", "aapl", "fb", "ibm", "msft"]
#symbols = ["amzn"]

"""url format, later we substitute each curly brackets by different values to scrape different data we need
first space is ticker (aapl, etc.), second space is type of data (income statement, balance sheet, etc.)"""
url_form = "http://www.nasdaq.com/symbol/{}/financials?query={}&data=quarterly" 

"""elements (html code) that contain financial data of interest are organized in the same way. General form is given as financials_xpath below
When the curly bracket (text() = '{}') is substituted by the name of financial data (Total Assets, Total Libilities, etc.),
the complete element is generated and can be searched directly. """
#find all td (standard cells) with parent tr (row) and grandparent tbody, 
#where the th (header cell) in the same row is the name of financial data we want to scrape

for i, symbol in enumerate(symbols): #"amzn"=0, "aapl"=1, etc.
    ## navigate to income statement quarterly page
    url = url_form.format(symbol, "ratios")
    browser.get(url)

    # Find page titles in h1 format (heading) with text containing "Company Financials"
    company_xpath = "//h1[contains(text(), ' Company Financials')]"
    company = browser.find_elements_by_xpath(company_xpath)[0].text

    #Find quarters by identifying th (header cells) under tr under thead, where first th item contains text "Quarter:"
    #we scrape only the third and later th items. There should be four items
    years_xpath = "//thead/tr[th[1][text() = 'Period Ending:']]/th[position()>=3]"
    elements = browser.find_elements_by_xpath(years_xpath) # find the elements according to conditions stated in xpath
    years = list(map(lambda x: x.text[-4:], elements))

    #Find quarters ending dates by identifying th (header cells) with parant tr (row) and grandparent thead,
    #where first th item contains text "Quarter Ending:"
    #we scrape only the third and later th items. There should be four items
    year_endings_xpath = "//thead/tr[th[1][text() = 'Period Ending:']]/th[position()>=3]"
    elements = browser.find_elements_by_xpath(year_endings_xpath) # find the elements according to conditions stated in xpath
    year_endings = list(map(lambda x: x.text, elements))



    # url = url_form.format(symbol, "income-statement")
    # browser.get(url)
    #
    # #Find page titles in h1 format (heading) with text containing "Company Financials"
    # company_xpath = "//h1[contains(text(), ' Company Financials')]"
    # company = browser.find_elements_by_xpath(company_xpath)[0].text
    #
    # #Find quarters by identifying th (header cells) under tr under thead, where first th item contains text "Quarter:"
    # #we scrape only the third and later th items. There should be four items
    # quarters_xpath = "//thead/tr[th[1][text() = 'Quarter:']]/th[position()>=3]"
    # elements = browser.find_elements_by_xpath(quarters_xpath) # find the elements according to conditions stated in xpath
    # quarters = list(map(lambda x: x.text, elements))

    # #Find quarters ending dates by identifying th (header cells) with parant tr (row) and grandparent thead,
    # #where first th item contains text "Quarter Ending:"
    # #we scrape only the third and later th items. There should be four items
    # quarter_endings_xpath = "//thead/tr[th[1][text() = 'Quarter Ending:']]/th[position()>=3]"
    # elements = browser.find_elements_by_xpath(quarter_endings_xpath) # find the elements according to conditions stated in xpath
    # quarter_endings = list(map(lambda x: x.text, elements))

    #Scrape total revenue, gross profit and net_income of each quarter, refer to financials_xpath format for details
    #header cell is "Total Revenue", find remaining four items in this row
    financials_xpath = "//tbody/tr/th[text() = '{}']/../td[contains(text(), '%')]"
    elements = browser.find_elements_by_xpath(financials_xpath.format("Current Ratio")) # find the elements according to conditions stated in xpath
    current_ratio = list(map(lambda x: x.text, elements))
    elements = browser.find_elements_by_xpath(
        financials_xpath.format("Quick Ratio"))  # find the elements according to conditions stated in xpath
    quick_ratio = list(map(lambda x: x.text, elements))
    elements = browser.find_elements_by_xpath(
        financials_xpath.format("Cash Ratio"))  # find the elements according to conditions stated in xpath
    cash_ratio = list(map(lambda x: x.text, elements))
    elements = browser.find_elements_by_xpath(
        financials_xpath.format("Gross Margin"))  # find the elements according to conditions stated in xpath
    gross_margin = list(map(lambda x: x.text, elements))
    elements = browser.find_elements_by_xpath(
        financials_xpath.format("Operating Margin"))  # find the elements according to conditions stated in xpath
    operating_margin = list(map(lambda x: x.text, elements))
    elements = browser.find_elements_by_xpath(
        financials_xpath.format("Pre-Tax Margin"))  # find the elements according to conditions stated in xpath
    pre_tex_margin = list(map(lambda x: x.text, elements))
    elements = browser.find_elements_by_xpath(
        financials_xpath.format("Profit Margin"))  # find the elements according to conditions stated in xpath
    profit_margin = list(map(lambda x: x.text, elements))
    elements = browser.find_elements_by_xpath(
        financials_xpath.format("Pre-Tax ROE"))  # find the elements according to conditions stated in xpath
    pre_tax_roe = list(map(lambda x: x.text, elements))
    elements = browser.find_elements_by_xpath(
        financials_xpath.format("After Tax ROE"))  # find the elements according to conditions stated in xpath
    after_tax_roe = list(map(lambda x: x.text, elements))


    # #Scrape total revenue, gross profit and net_income of each quarter, refer to financials_xpath format for details
    # #header cell is "Total Revenue", find remaining four items in this row
    # financials_xpath = "//tbody/tr/th[text() = '{}']/../td[contains(text(), '$')]"
    # elements = browser.find_elements_by_xpath(financials_xpath.format("Total Revenue")) # find the elements according to conditions stated in xpath
    # total_revenue = list(map(lambda x: x.text, elements))
    #
    # #header cell is "Gross Profit", find remaining four items in this row
    # elements = browser.find_elements_by_xpath(financials_xpath.format("Gross Profit")) # find the elements according to conditions stated in xpath
    # gross_profit = list(map(lambda x: x.text, elements))
    #
    # #header cell is "Net Income", find remaining four items in this row
    # elements = browser.find_elements_by_xpath(financials_xpath.format("Net Income")) # find the elements according to conditions stated in xpath
    # net_income = list(map(lambda x: x.text, elements))
    #
    # ## navigate to balance sheet quarterly page
    # url = url_form.format(symbol, "balance-sheet")
    # browser.get(url)
    #
    # elements = browser.find_elements_by_xpath(financials_xpath.format("Total Assets")) # find the elements according to conditions stated in xpath
    # total_assets = list(map(lambda x: x.text, elements))
    #
    # elements = browser.find_elements_by_xpath(financials_xpath.format("Total Liabilities")) # find the elements according to conditions stated in xpath
    # total_liabilities = list(map(lambda x: x.text, elements))
    #
    # elements = browser.find_elements_by_xpath(financials_xpath.format("Total Equity")) # find the elements according to conditions stated in xpath
    # total_equity = list(map(lambda x: x.text, elements))
    #
    # ## navigate to cash flow quarterly page
    # url = url_form.format(symbol, "cash-flow")
    # browser.get(url)
    #
    # elements = browser.find_elements_by_xpath(financials_xpath.format("Net Cash Flow")) # find the elements according to conditions stated in xpath
    # net_cash_flow = list(map(lambda x: x.text, elements))

## fill the datarame with the scraped data, 4 rows per company
    for j in range(4):  
        row = (i * 4) + j
        df.loc[row, 'company'] = company
        df.loc[row, 'years'] = years[j]
        df.loc[row, 'year_endings'] = year_endings[j]
        # df.loc[row, 'total_revenue'] = total_revenue[j]
        # df.loc[row, 'gross_profit'] = gross_profit[j]
        # df.loc[row, 'net_income'] = net_income[j]
        # df.loc[row, 'total_assets'] = total_assets[j]
        # df.loc[row, 'total_liabilities'] = total_liabilities[j]
        # df.loc[row, 'total_equity'] = total_equity[j]
        # df.loc[row, 'net_cash_flow'] = net_cash_flow[j]
        df.loc[row, 'current_ratio'] = current_ratio[j]
        df.loc[row, 'quick_ratio'] = quick_ratio[j]
        df.loc[row, 'cash_ratio'] = cash_ratio[j]
        df.loc[row, 'gross_margin'] = gross_margin[j]
        df.loc[row, 'operating_margin'] = operating_margin[j]
        df.loc[row, 'pre_tex_margin'] = pre_tex_margin[j]
        df.loc[row, 'profit_margin'] = profit_margin[j]
        df.loc[row, 'pre_tax_roe'] = pre_tax_roe[j]
        df.loc[row, 'after_tax_roe'] = after_tax_roe[j]

browser.quit()
 
## create a csv file in our working directory with our scraped data
df.to_csv("company financials.csv", index=False)
print('Scraping is done!')
