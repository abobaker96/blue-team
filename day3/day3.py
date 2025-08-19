import os, time
import requests
BASE ="https://httpbin.org"

respons =requests.get(
    f"{BASE}/user-agent",
    timeout=5
)
respons.raise_for_status()
status =respons.status_code
content =respons.headers["content-type"]
data =respons.json()
#print(data)
#print(data[user-agent])



response1 =requests.post(
    f"{BASE}/response-headers",
    params={'freeform':'test'},
    timeout=5
)
response1.raise_for_status
content =response1.headers['content-type']
data=response1.json()
#print(data)
 
with requests.session() as s:
    for i in range(3):
        r=s.get(f"{BASE}/user-agent",timeout=5)
        x=s.get(f"{BASE}/IP")
        if r.status_code == 200 and x.status_code == 200:
           break

  #  print(r.status_code)
  #  print(r.json)
   # print(x.json)
