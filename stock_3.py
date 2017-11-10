#!/usr/bin/python
#coding:utf-8

#601398

import datetime as dt
import tushare as ts
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


start = dt.datetime(2015,1,1)
start_date = start.strftime('%Y-%m-%d')
end = dt.datetime(2017,12,31)
end_date = end.strftime('%Y-%m-%d')
df_his = ts.get_hist_data('601398',start_date,end_date) 
df_his.to_csv('TSLA.csv')

#df = pd.read_csv('TSLA.csv', parse_dates=True, index_col=0)
#df.plot()
#plt.show()
#df['Adj Close'].plot()

#print(df[['high']])

#df[['high','low']].plot()
#plt.show()
