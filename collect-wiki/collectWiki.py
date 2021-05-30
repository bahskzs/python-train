import pandas as pd
import datetime

from handle_db import HandleMysql
from log import LogUtil
import time

# 读取文件
df = pd.read_csv("H:\software\My Research Folder.csv")
# 找出是今天收集的
data = df[df["Date"] == str(datetime.date.today())]
data["collect_date"] = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

try:
    engine = HandleMysql().conn_mysql()
    data.to_sql(name='t_collect', con=engine, if_exists='append', index=False, index_label=False)
    LogUtil.info(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + " Success write to database ," + str(
        len(data)) + " records")
except:
    LogUtil.info("write to database fail ...")
    raise Exception("Invalid level!")
