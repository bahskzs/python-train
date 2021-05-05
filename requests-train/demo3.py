import requests

token_url="http://imp.apexinfo.com.cn/welcome.do"


res = requests.get(url=token_url)



login_session = requests.session()
