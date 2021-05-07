from lxml import etree
import pandas as pd
import datetime
from handleDB import HandleMysql
import grequests
import requests
import time
import numpy as np


# 获取昨天
def getYesterday():
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday


# start_time = time.time()

col_list = ["美元", "欧元"]

request_url = 'https://srh.bankofchina.com/search/whpj/search_cn.jsp'

# req_list = [  # 请求列表
#     grequests.get(request_url,
#                   params={
#                       "erectDate": getYesterday(),
#                       "nothing": getYesterday(),
#                       "pjname": col_list[0]
#                   }),
#     grequests.get(request_url,
#                   params={
#                       "erectDate": getYesterday(),
#                       "nothing": getYesterday(),
#                       "pjname": col_list[1]
#                   })
# ]
req_list=[]

csv_data = pd.read_csv("date_data.csv", low_memory=False)  # 防止弹出警告
csv_df = pd.DataFrame(csv_data).values.tolist()
for dateStr in csv_df:
    param_data = {
        "erectDate": dateStr,
        "nothing": dateStr,
        "pjname": col_list[0]
    }
    req = grequests.get(request_url,params=param_data)
    req_list.append(req)
    param_data = {
        "erectDate": dateStr,
        "nothing": dateStr,
        "pjname": col_list[1]
    }
    req = grequests.get(request_url, params=param_data)
    req_list.append(req)

res_list = grequests.map(req_list)

arr = []
# end_time = time.time()
# print((time.time()-start_time))
for res_text in res_list:
    html = etree.HTML(res_text.text)
    content = html.xpath("//tr[2]/td[position()=1 or position()>5]/text()")
    # 采集时间
    content.append(datetime.date.today())
    arr.append(content)

# 转换格式
data = np.array(arr)
df = pd.DataFrame(data=data, columns=['money_type', 'cur_price', 'published_time', 'collection_time'])

engine = HandleMysql().conn_mysql()
df.to_sql(name='rate_data', con=engine, if_exists='append', index=False, index_label=False)
