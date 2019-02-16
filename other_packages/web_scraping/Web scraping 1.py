# -*- coding: utf-8 -*-
"""
First web scraping example
Created on Sat Apr 14 00:37:00 2018

@author: Frankie Ho
"""

#Import beautiful soup, requests and pandas
import bs4 as bs
import requests
import pandas as pd
import os

path = r'C:\便捷\工作\Code\Python\AFPD\other_packages\web_scraping'

#Define function to download a list of S&P 500 companies with ticker and company name information, then save as .csv file
def save_sp500_tickers():  
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies') #Assess this wikipedia page with list of S&P 500 companies
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'}) #Find tables in this page
    tickers = [] #save tickers column here
    securities = [] #save securities column here
    sectors = []
    sub_industries = []
    locations = []
    dates = []
    for row in table.findAll('tr')[1:]: #Each row is identified by header ('tr') in html code. 
        ticker = row.findAll('td')[0].text #For each row in the table, find the first standard cell ('td') (first column)
        security = row.findAll('td')[1].text #For each row in the table, find the second standard cell ('td') (second column)
        sector = row.findAll('td')[3].text
        sub_industry = row.findAll('td')[4].text
        location = row.findAll('td')[5].text
        date = row.findAll('td')[6].text
        tickers.append(ticker)
        securities.append(security)
        sectors.append(sector)
        sub_industries.append(sub_industry)
        locations.append(location)
        dates.append(date)
    df = pd.DataFrame({'ticker':tickers, 'security':securities, 'sector':sectors,'sub industry':sub_industries,'location':locations,'date':dates})
    df_new = df[['ticker', 'security','sector','sub industry','location','date']] #Switch column order
    df_new.to_csv(path + os.sep + "sp500 stock list.csv", index = False) #Save dataframe as csv file

if __name__=="__main__":
    save_sp500_tickers() 
    
