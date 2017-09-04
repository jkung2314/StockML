import numpy as np
import pandas as pd
from sklearn.svm import SVR
#import pandas_datareader.data as web
import quandl
import datetime as dt

start = dt.date(2017,5,20)
end = dt.date(2017,8,3)
print(start)
print(end)

#Reads in data from Google Finance
#df = web.DataReader("AAPL",'google',start,end)

#Reads in data from Quandl
df = quandl.get("DCE/JMK2018", start_date = start, end_date = end)
prices = df["Close"].values
total_rows = df['Close'].count()
dates = [None] * total_rows
df2 = df.rolling(50).mean()

#Normalizes date values to correspond with price of stock
for i in range(0,total_rows):
    dates[i] = i
    i = i+1

print "\n\n\n"

if np.isnan(df2["Close"].iloc[-1]): #If Security has not been trading for 50 days
    print "Optimal Stop Loss Value Cannot Be Calculated"
    print "Stop Loss Value Calculated with", total_rows, "Day Moving Average:"
    df2 = df.rolling(total_rows).mean()
    print (df2["Close"].iloc[-1])
else:
    print "Optimal Stop Loss: ",df2["Close"].iloc[-1]

percentage = (df["Close"].iloc[-1] - df2["Close"].iloc[-1]) / df["Close"].iloc[-1] *100
print "Stop loss value is:", percentage, "%", "from current price"
