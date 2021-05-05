# -*- coding: utf-8 -*-

"""
抓取中国银行汇率
Created on 2021/05/05

@author:bahskzs

"""

import requests
from lxml import etree
import pandas as pd
import datetime
from sqlalchemy import create_engine
from readConfig import ReadConfig


# 获取昨天
def getYesterday():
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday


# 货币
money_type = "美元"

data = {
    "erectDate": getYesterday(),
    "nothing": getYesterday(),
    "pjname": money_type
}

# 获取页面
res = requests.get(url="https://srh.bankofchina.com/search/whpj/search_cn.jsp", params=data)
html = etree.HTML(res.text)
arr_dollar = html.xpath("//tr[2]/td[position()>5]/text()")

money_type = "欧元"

res = requests.get(url="https://srh.bankofchina.com/search/whpj/search_cn.jsp", params=data)
html = etree.HTML(res.text)
arr_euro = html.xpath("//tr[2]/td[position()>5]/text()")

# 构造映射关系
listZip = list(zip(arr_dollar, arr_euro))
# df = pd.DataFrame()

# 构造数据
price_data = {
    'money_type': ["美元", "欧元"],
    'cur_price': listZip[0],
    'published_time': listZip[1],
    'collection_time': [datetime.date.today(), datetime.date.today()]
}

# 转换为df
df = pd.DataFrame(price_data)


mysqlUrl = "mysql+pymysql://" + ReadConfig.getConfigValue("user") + ":" + ReadConfig.getConfigValue(
    "passwd") + "@" + ReadConfig.getConfigValue("host") + ":" + ReadConfig.getConfigValue(
    "port") + "/" + ReadConfig.getConfigValue("database") + "?charset=utf8"

# 利用df的.to_sql方法写入数据库
engine = create_engine(mysqlUrl)
df.to_sql(name='rate_demo', con=engine, if_exists='append', index=False, index_label=False)


