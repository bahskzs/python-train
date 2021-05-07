# -*- coding: utf-8 -*-

"""
读取 demo.docx 中的表格的内容
Created on 2021/05/06
@author : bahskzs
"""

import docx
from docx import Document
import pandas as pd

# 读取文件
docFile = "demo.docx"
document = Document(docFile)

# 获取文件中的表格
tables = document.tables
table = tables[0]

# df = pd.DataFrame(table.rows)
content = list()

# 遍历表格中的内容
for i, row in enumerate(table.rows):
    cell_content = list()
    for cell in row.cells:
        cell_content.append(cell.text)
    content.append(cell_content)

df = pd.DataFrame(content)
print(df)

