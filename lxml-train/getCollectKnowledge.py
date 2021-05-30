from lxml import etree
import requests
import pandas as pd
import datetime
import time
import numpy as np
import logging
import ssl

from log import LogUtil

"""
爬取weave的页面
Created on 2021/05/30

@author : bahskzs

"""

request_url = 'https://www.weavatools.com/app/dashboard;cid=-MawEUJVj51nAvQl3zqq'

header = {
    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    "Accept": "Accept: text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/74.0.3724.8 Safari/537.36",
    "x-amazon-user-agent": "AmazonJavascriptScratchpad/1.0 (Language=Javascript)",
    "X-Requested-With": "XMLHttpRequest"
}

res_list = requests.get(request_url, headers=header, params={

  "access_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjMwMjUxYWIxYTJmYzFkMzllNDMwMWNhYjc1OTZkNDQ5ZDgwNDI1ZjYiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiQ2F0IE9yYW5nZSIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS93cml0aW8tMTM0MSIsImF1ZCI6IndyaXRpby0xMzQxIiwiYXV0aF90aW1lIjoxNjIyMzYwODQxLCJ1c2VyX2lkIjoiRld4aURmYVVLTFo3Q1VVZ01La2xwbVBLTEhvMiIsInN1YiI6IkZXeGlEZmFVS0xaN0NVVWdNS2tscG1QS0xIbzIiLCJpYXQiOjE2MjIzODA4MDcsImV4cCI6MTYyMjM4NDQwNywiZW1haWwiOiJiYWhza3pzNjEwQGxpdmUuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsiYmFoc2t6czYxMEBsaXZlLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.GK2qjN7RW7gd-ywQDH0G44NEBLOW7ft4DXG955vZJ9xnuHxaGqNUdmj4yuI41BW2VTh28ja4ra8KbpBHmD0MGVexyUemZs9UOTjtSRMTh8cUynYmEjQu4YYw7o0IeKCcOjnRr60uPTDeh7vIekKW4cSf3h11oI-2GvjNbMquIdQh6vS8l61LYKZ70ICYT0d-7CFNC0StHurugDQxaLNtbNagYxka85gu40udaTBd6cd7PQkfP-4VlHdvnnk1aI15-LOaMUOM-AYRnLwfUXJ_XBMxPo3HaC_JAui5z4aO1fKTlGP5fFL2Qt9DRkK9VXKwcWY-90mmM1ev6RUOf9cRxg",
  "expires_in": "3600",
  "token_type": "Bearer",
  "refresh_token": "AGEhc0DPzXQ46f8QRwz_HXiVFlINMFJeHavJ1nnavZCFlWEP4fuO0sayXxuE066OvMT_owhiIAW_dPwYJ-FyrgJ55Uh9QgiwAwbak_T3YvNPoZuKUbB7hq7qr78fzI3kwdbGmtjAEdGZlFP_XP7tgoFLL3D0D5b5xXCtVdDALlZA1BMqhDCqK26-EOL1VvDAEzqcDdjtDyrY",
  "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjMwMjUxYWIxYTJmYzFkMzllNDMwMWNhYjc1OTZkNDQ5ZDgwNDI1ZjYiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiQ2F0IE9yYW5nZSIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS93cml0aW8tMTM0MSIsImF1ZCI6IndyaXRpby0xMzQxIiwiYXV0aF90aW1lIjoxNjIyMzYwODQxLCJ1c2VyX2lkIjoiRld4aURmYVVLTFo3Q1VVZ01La2xwbVBLTEhvMiIsInN1YiI6IkZXeGlEZmFVS0xaN0NVVWdNS2tscG1QS0xIbzIiLCJpYXQiOjE2MjIzODA4MDcsImV4cCI6MTYyMjM4NDQwNywiZW1haWwiOiJiYWhza3pzNjEwQGxpdmUuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsiYmFoc2t6czYxMEBsaXZlLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.GK2qjN7RW7gd-ywQDH0G44NEBLOW7ft4DXG955vZJ9xnuHxaGqNUdmj4yuI41BW2VTh28ja4ra8KbpBHmD0MGVexyUemZs9UOTjtSRMTh8cUynYmEjQu4YYw7o0IeKCcOjnRr60uPTDeh7vIekKW4cSf3h11oI-2GvjNbMquIdQh6vS8l61LYKZ70ICYT0d-7CFNC0StHurugDQxaLNtbNagYxka85gu40udaTBd6cd7PQkfP-4VlHdvnnk1aI15-LOaMUOM-AYRnLwfUXJ_XBMxPo3HaC_JAui5z4aO1fKTlGP5fFL2Qt9DRkK9VXKwcWY-90mmM1ev6RUOf9cRxg",
  "user_id": "FWxiDfaUKLZ7CUUgMKklpmPKLHo2",
  "project_id": "617911510552"

    })
html = etree.HTML(res_list.text)
LogUtil.info(" html的格式 " + str(res_list.text))
content = html.xpath("//app-website-list")
LogUtil.info(" content的格式 " + str(content))

