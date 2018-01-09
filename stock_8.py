#coding: utf-8

import re
from urllib2 import urlopen
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
df_his = ts.get_hist_data('002558',start_date,end_date) 
df_his.to_csv("002558.csv")
