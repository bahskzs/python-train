# -*- coding: utf-8 -*-
import pandas as pd

from log import LogUtil

"""
读取excel
Created on 2021/05/16

@author:bahskzs

"""

io = r'H:\software\个人学习类任务设计.xlsx'
data = pd.read_excel(io, sheet_name='5月学习计划_1', header=0 #,
                     #names=['序号', '任务内容', '具体步骤及检验方法', '学习资料', 'DDL', '金币数量', '推荐资料寻找方式', '是否可放弃本期任务', '放弃缘由']
)
LogUtil.info(" data: ")
print(data)
