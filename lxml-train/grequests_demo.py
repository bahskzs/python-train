# -*- coding: utf-8 -*-

from lxml import etree
import pandas as pd
import datetime
from handleDB import HandleMysql
import grequests
import time
import numpy as np
import logging

"""
爬取外汇
Created on 2021/05/05

@author : bahskzs

"""

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# 获取昨天
def getYesterday():
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday


# start_time = time.time()

col_list = ["美元", "欧元"]

request_url = 'https://srh.bankofchina.com/search/whpj/search_cn.jsp'

header = {
    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    "Accept": "Accept: text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/74.0.3724.8 Safari/537.36",
    "x-amazon-user-agent": "AmazonJavascriptScratchpad/1.0 (Language=Javascript)",
    "X-Requested-With": "XMLHttpRequest"
}

req_list = [  # 请求列表
    grequests.get(request_url, headers=header,
                  params={
                      "erectDate": getYesterday(),
                      "nothing": getYesterday(),
                      "pjname": col_list[0]
                  }),
    grequests.get(request_url, headers=header,
                  params={
                      "erectDate": getYesterday(),
                      "nothing": getYesterday(),
                      "pjname": col_list[1]
                  })
]
# req_list=[]

# csv_data = pd.read_csv("date_data.csv", low_memory=False)  # 防止弹出警告
# csv_df = pd.DataFrame(csv_data).values.tolist()
# for dateStr in csv_df:
#     param_data = {
#         "erectDate": dateStr,
#         "nothing": dateStr,
#         "pjname": col_list[0]
#     }
#     req = grequests.get(request_url,params=param_data)
#     req_list.append(req)
#     param_data = {
#         "erectDate": dateStr,
#         "nothing": dateStr,
#         "pjname": col_list[1]
#     }
#     req = grequests.get(request_url, params=param_data)
#     req_list.append(req)


start_time = time.time()
arr = []
try:
    logger.info(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + " 开始爬取...")
    res_list = grequests.map(req_list)
    diff_time = time.time() - start_time

    for res_text in res_list:
        html = etree.HTML(res_text.text)
        content = html.xpath("//tr[2]/td[position()=1 or position()>5]/text()")
        logger.info("return content: " + str(content))
        # 采集时间
        content.append(datetime.date.today())
        arr.append(content)
    logger.info('Success ,本次花费:' + str(diff_time) + "...")
    logger.info("datas: " + str(arr))
except:
    logger.error('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')

# 转换格式
data = np.array(arr)
df = pd.DataFrame(data=data, columns=['money_type', 'cur_price', 'published_time', 'collection_time'])

engine = HandleMysql().conn_mysql()
try:
    df.to_sql(name='rate_data', con=engine, if_exists='append', index=False, index_label=False)
    logger.info(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + " Success write to database ," + str(
        len(df)) + " records")
except:
    logger.error("write to database fail ...")
    raise Exception("Invalid level!")
