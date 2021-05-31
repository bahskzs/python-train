import pandas as pd
import datetime

from handle_db import HandleMysql
from log import LogUtil
import time

# 读取文件
df = pd.read_csv("H:\Downloads\My Research Folder.csv")
# 找出是今天收集的
today=str(datetime.date.today())
data = df[df["Date"] == today]
collectDate = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
data["collect_date"] = collectDate

try:
    engine = HandleMysql().conn_mysql()
    # 每天处理的时候都把当天相关记录清除后再追加内容
    engine.execute("delete from t_collect where Date = '{collectDate}'".format(
        collectDate=str(datetime.date.today())
    ))
    data.to_sql(name='t_collect', con=engine, if_exists='append', index=False, index_label=False)
    LogUtil.info(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + " Success write to database ," + str(
        len(data)) + " records")
except:
    LogUtil.info("write to database fail ...")
    raise Exception("Invalid level!")
