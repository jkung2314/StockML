import numpy as np
import pandas as pd
from sklearn.svm import SVR
import pandas_datareader.data as web
import quandl
import datetime as dt

start = dt.date(2017,1,1)
end = dt.date(2017,8,31)
print(start)
print(end)

#Reads in data from Google Finance
#df = web.DataReader("AAPL",'google',start,end)

#Reads in data from Quandl / Quandl Codes are found on quandl.com
df = quandl.get("DCE/PPV2017", start_date = start, end_date = end)
total_rows = df['Close'].count()
print df

#DataFrame for Rolling Mean (50 Day Moving Average)
dfm = df.rolling(50).mean()

#Backtest function utilizing 50 Day Moving Average Algorithm
def Backtest(df,dfm,total_rows):
    flag = False #Indicator for whether there are shares in portfolio
    for i in range(0,total_rows): #Iterating through each day (Backtesting)
        #If Open Price > Moving Average and no shares in portfolio, Buy
        if df["Open"].iloc[i] > dfm["Close"].iloc[i] and flag == False:
            print "Buying:",df["Open"].iloc[i]
            flag = True #Shares in portfolio = True
        #If Open Price < Moving Average and there are shares in portfolio, Sell
        elif df["Open"].iloc[i] < dfm["Close"].iloc[i] and flag == True:
            print "Selling:",df["Open"].iloc[i]
            flag = False #Shares in portfolio = False

    print "Current Price:",df["Close"].iloc[-1]

#Function to calculate benchmark gains if security was to be held from
#   start date +50 days to end date.
#   Benchmark gain is calculated starting from 50 days after start date
#   due to the fact that 50 day moving average cannot be calculated
#   until 50 days after start date
def Benchmark(df):
    diff = df["Close"].iloc[-1]-df["Close"].iloc[50]
    percentage_gain = diff / df["Close"].iloc[-1] * 100
    print percentage_gain, "%", "Benchmark Gain"

print "\n\n\n"
Backtest(df,dfm,total_rows)
Benchmark(df)
