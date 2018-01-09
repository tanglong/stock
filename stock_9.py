#coding: utf-8

import re
from urllib2 import urlopen
import datetime as dt
import tushare as ts
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


stock_CodeUrl = 'http://quote.eastmoney.com/stocklist.html'

def urlTolist(url):
    allCodeList = []
    html = urlopen(url).read()
    html = html.decode('gbk')
    s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">(.*?)</a></li>'
    pat = re.compile(s)
    code = pat.findall(html)
    for item in code:
        #print(item[1])
        if item[0][0]=='6' or item[0][0]=='3' or item[0][0]=='0':
            allCodeList.append(item)
    return allCodeList

start = dt.datetime(2010,1,1)
start_date = start.strftime('%Y-%m-%d')
end = dt.datetime(2017,12,31)
end_date = end.strftime('%Y-%m-%d')

allCodelist = urlTolist(stock_CodeUrl)
for code in allCodelist:
        print(code[1])
        print(code[0])
        print(type(code[1]))
        df_his = ts.get_hist_data(code[0],start_date,end_date)
        #print(df_his)
        if df_his is not None :
            name = code[0] + '.csv'
            df_his.to_csv(name)
