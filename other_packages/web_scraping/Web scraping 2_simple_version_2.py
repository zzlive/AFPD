# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 00:35:04 2018

@author: Frankie Ho
"""

## Scraping financial data using Selenium and beautifulsoup, import packages first
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import re

"""
Objective: Scrape quarterly financial information (Income statement and balance sheet) of listed companies
"""

## create a pandas dataframe to store the scraped data
df = pd.DataFrame(index=range(20),
                  columns=['company', 'quarter', 'quarter_ending', 
                           'total_revenue', 'gross_profit', 'net_income', 
                           'total_assets', 'total_liabilities', 'total_equity', 
                           'net_cash_flow'])

## launch the Chrome/Firefox browser
## Please change directory to the location of your Chromedriver.exe (or geckodriver.exe) file and save that as my_path
my_path = r"D:\OneDrive - The University Of Hong Kong\HKU TA\Fall 2018-2019\FINA2390\MicrosoftWebDriver.exe"
browser = webdriver.Edge(executable_path=my_path)
browser.maximize_window()


"""url format, later we substitute each curly brackets by different values to scrape different data we need
first space is ticker (aapl, etc.), second space is type of data (income statement, balance sheet, etc.)"""
url_form = "http://www.nasdaq.com/symbol/{}/financials?query={}&data=quarterly" 


"""Scrape several financial variables of five stocks with a for loop and get_elements function defined above. 
Save results in a dataframe"""       
## company ticker symbols, Here we have Amazon, Apple, Facebook, IBM and Microsoft
symbols = ['amzn', 'aapl', 'fb', 'ibm', 'msft']
        
for i, symbol in enumerate(symbols): #"amzn"=0, "aapl"=1, etc.
    ## navigate to income statement quarterly page    
    url = url_form.format(symbol, "income-statement")
    browser.get(url) #load page using selenium
    soup = BeautifulSoup(browser.page_source, 'lxml') #use beautifulsoup to parse page
    
    ## Find page titles in h1 format (heading) with text containing "Company Financials"
    company = soup.find('h1',string=re.compile('Company Financials')).text       
    
    ## Find titles from parsed page by identifying th (header cells) where first th item (identifier) contains text as title argument
    ## we scrape only the third and later th items. There should be four items
    ## Find quarters by get_titles function with identifier cell's text as 'Quarter:'
    titles = soup.find('th', string='Quarter:').find_next_siblings('th')[1:]
    quarters = list(map(lambda x: x.text, titles))

    ## Find quarter_endings by get_titles function with identifier cell's text as 'Quarter Ending:'
    titles = soup.find('th', string='Quarter Ending:').find_next_siblings('th')[1:]
    quarter_endings = list(map(lambda x: x.text, titles))

    ## Find total_revenue with row header cell's text as 'Total Revenue'
    ## Find elements from parsed page by identifying td cells containing "$", 
    ## where they are siblings of th (header cell) with text identical to financial argument
    ## There should be four items
    elements = soup.find('th', string='Total Revenue').find_next_siblings('td', string=re.compile('\$')) 
    total_revenue = list(map(lambda x: x.text, elements))
    
    ## Find gross profit with row header cell's text as 'Gross Profit'
    elements = soup.find('th', string='Gross Profit').find_next_siblings('td', string=re.compile('\$')) 
    gross_profit = list(map(lambda x: x.text, elements))
    
    ## Find net_income with row header cell's text as 'Net Income'
    elements = soup.find('th', string='Net Income').find_next_siblings('td', string=re.compile('\$')) 
    net_income = list(map(lambda x: x.text, elements))
        
    ## navigate to balance sheet quarterly page 
    url = url_form.format(symbol, 'balance-sheet')
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    
    elements = soup.find('th', string='Total Assets').find_next_siblings('td', string=re.compile('\$')) 
    total_assets = list(map(lambda x: x.text, elements))
    
    elements = soup.find('th', string='Total Liabilities').find_next_siblings('td', string=re.compile('\$')) 
    total_liabilities = list(map(lambda x: x.text, elements))
    
    elements = soup.find('th', string='Total Equity').find_next_siblings('td', string=re.compile('\$')) 
    total_equity = list(map(lambda x: x.text, elements))
        
    ## navigate to cash flow quarterly page 
    url = url_form.format(symbol, 'cash-flow')
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    
    elements = soup.find('th', string='Net Cash Flow').find_next_siblings('td', string=re.compile('\$')) 
    net_cash_flow = list(map(lambda x: x.text, elements))

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
df.to_csv('company financials.csv', index=False)
print('Scraping is done!')
    
