import requests
import time

start_time = time.time()
res = requests.get(url="http://httpbin.org/ip")
print(res.text)
end_time = time.time()
print(end_time-start_time)