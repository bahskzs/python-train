# -*- coding: utf-8 -*-
"""
抓取中国银行汇率
Created on 2021/05/05

@author:bahskzs

"""

import requests
import lxml
from lxml import etree
import pandas as pd
import datetime

# 获取昨天
def getYesterday():
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday


data = {
    "erectDate": getYesterday(),
    "nothing": getYesterday(),
    "pjname": "美元",
    "page": "1"
}
res = requests.get(url="https://srh.bankofchina.com/search/whpj/search_cn.jsp", params=data)
print(res.url)
# print(res.text)

html = etree.HTML(res.text)
# print(etree.tostring(html).decode())
print(html.xpath("boolean(//tr[2]/td[position()>5]/text())"))
arr_dollar = html.xpath("//tr[2]/td[position()>5]/text()")
# print(arr_dollar)

# ['646.72', '2021.05.04 21:00:04']  返回值 arr[0],arr[1]


arr_euro = ['784.43', '2021.05.04 21:00:04']
listZip = list(zip(arr_dollar, arr_euro))
# df = pd.DataFrame()

price_data = {
    'cur_price': listZip[0],
    'published_time': listZip[1]
}

df = pd.DataFrame(price_data)
#   cur_price       published_time
# 0    646.72  2021.05.04 21:00:04
# 1    784.43  2021.05.04 21:00:04
print(df)

# df 转二维数组
# [['646.72' '2021.05.04 21:00:04']
#  ['784.43' '2021.05.04 21:00:04']]
print(df.values)



