import numpy as np
import pandas as pd
from sklearn.svm import SVR
import pandas_datareader.data as web
import datetime as dt

start = dt.date(2017,6,1)
end = dt.date(2017,7,6)
print(start)
print(end)
#df = pd.read_csv("AAPL.csv")
#Reads in data from Google Finance
df = web.DataReader("AAPL",'google',start,end)
print(df)
#dates = df["Date"].values
#dates = df.index.values
prices = df["Open"].values
total_rows = df['Open'].count()
dates = [None] * total_rows

#Normalizes date values to correspond with price of stock
for i in range(0,total_rows):
    dates[i] = i
    i = i+1
print(total_rows)

#SVR Price Prediction
def predict_prices(dates, prices, x):
    dates = np.reshape(dates,(len(dates),1))
    clf = SVR(kernel = "rbf",C=1e3, gamma = 0.1)
    clf.fit(dates,prices)
    return clf.predict(x)[0]

#total_rows Parameter is set for next day stock price calculation
predicted_price = predict_prices(dates,prices,total_rows)
print(predicted_price)
