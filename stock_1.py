#!/usr/bin/python
#coding:utf-8

import tushare as ts
df_his = ts.get_hist_data('601313') 
print(df_his)
