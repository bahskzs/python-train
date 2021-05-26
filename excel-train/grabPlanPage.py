# -*- coding: utf-8 -*-
import requests

request_url = 'https://docs.qq.com/sheet/DVmNZY0JKWEtRTkJa'

res = requests.get(url=request_url)
print(res.text)