import numpy as np
import pandas as pd
from sklearn.svm import SVR
import pandas_datareader.data as web
import quandl
import datetime as dt

start = dt.date(2017,7,28)
end = dt.date(2017,8,3)

print(start)
print(end)

#Reads in data from Google Finance
df = web.DataReader("AAPL",'google',start,end)

#Reads in data from Quandl
#df = quandl.get("DCE/JMK2018", start_date = start, end_date = end)

prices = df["Close"].values
total_rows = df['Close'].count()
dates = [None] * total_rows

#Normalizes date values to correspond with price of stock
for i in range(0,total_rows):
    dates[i] = i

#SVR Price Prediction
def predict_prices(dates, prices, x):
    dates = np.reshape(dates,(len(dates),1))
    clf = SVR(kernel = "rbf",C=1e3, gamma = 0.1)
    clf.fit(dates,prices)
    print "Predicted Price Tomorrow: $",clf.predict(x)[0]
    print"Accuracy is:" , (clf.score(dates,prices)*100),"%"

#total_rows Parameter is set for next day stock price calculation
print("\n\n\n")
print "Current Price: $", df["Close"].iloc[-1]
predict_prices(dates,prices,total_rows)
