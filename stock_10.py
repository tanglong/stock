#!/usr/bin/python
#coding:utf-8

import tushare as ts
df_his = ts.get_hist_data('000799') 
print(df_his)
