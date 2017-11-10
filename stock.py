#!/usr/bin/python
#coding:utf-8

import tushare as ts
df_his = ts.get_hist_data('601398') #招商银行 600036
print(df_his)
