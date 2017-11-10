#coding: utf-8

import re
from urllib2 import urlopen

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


allCodelist = urlTolist(stock_CodeUrl)
for code in allCodelist:
    if u"银行" in code[1]:
        print(code[1])
