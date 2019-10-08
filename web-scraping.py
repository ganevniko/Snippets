from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd
import time

#Creating a list of tickers
#----------------------------------------------------------------------------------------------------------------------------------------------
tickers=['AAPL', 'FB', 'NFLX', 'GOOG']

#Selecting features from each page
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
features1 = ['Market Cap', 'EPS (TTM)']
features2 = ['Enterprise Value',  'Trailing P/E','Payout Ratio']

#Creating our empty data frame
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
columns= features1 + features2

df = pd.DataFrame(columns=columns)# Create Padas DataFrame with the column names we picked

idx = 0
new_col = tickers  
df.insert(loc=idx, column='Tickers', value=new_col)

for tic in tickers:
    
    #Create two variables for the the two urls and generalize to tickers using '.format()' function
    url1= 'https://finance.yahoo.com/quote/{0}?p={0}&.tsrc=fin-srch'.format(tic)
    url2= 'https://finance.yahoo.com/quote/{0}/key-statistics?p={0}'.format(tic)
    
    #Connect to first url, read first page, parse and create list of td HTML section to look through for our features
    uClient1 = uReq(url1)
    page_html1 = uClient1.read()
    page_soup1 = soup(page_html1, 'html.parser')
    page_stat1 = page_soup1.findAll('td')
    
    
    #loop over features
    for feature in features1:
        for i in range(len(page_stat1)):
            if page_stat1[i].text.__contains__(feature):
                df[feature][df.Tickers == tic] = page_stat1[i+1].text
                
    
    #Connect to second url, read first page, parse and create list of td HTML section to look through for our features
    uClient2 = uReq(url2)
    page_html2 = uClient2.read()
    page_soup2 = soup(page_html2, 'html.parser')
    page_stat2 = page_soup2.findAll('td')
    
    #Copy paste previous loop over featuers
    for feature in features2:
        for i in range(len(page_stat2)):
            if page_stat2[i].text.__contains__(feature):
                df[feature][df.Tickers == tic] = page_stat2[i+1].text

df
