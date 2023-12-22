#
#   dont skid!
#   use before its patched
#   t.me/x6out
#   source below
#

import os
import threading
import json
import subprocess as sp
import requests
import uuid
import sys

with open("config.json") as f:
    config = json.load(f)

if not os.path.exists("promos.txt"):
  with open("promos.txt", "w") as file:
    pass

threads = config['threads']
prx = config['proxy']

os.system('cls')
if prx == "leaveblanktousenoproxies":
  print(f"Config: {threads} Threads | Proxy: No Proxies | https://t.me/x6out")
else:
  print(f"Config: {threads} Threads | Proxy: {prx} | https://t.me/x6out")

def worker():
  while True:
    url = 'https://api.discord.gx.games/v1/direct-fulfillment'
    headers = {
        "authority": "api.discord.gx.games",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://www.opera.com",
        "referer": "https://www.opera.com/",
        "sec-ch-ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"
    }
    nonce = uuid.uuid4()
    payload = {"partnerUserId": f"{nonce}"}
    if prx == "leaveblanktousenoproxies":
      response = requests.post(url, json=payload, headers=headers)
      if response.status_code == 200:
        p = response.json()['token']
        pr = f"https://discord.com/billing/promotions/partner-promotions/1180231712274387115/{p}"
        with open("promos.txt", "a") as file:
          file.write(pr + "\n")
      else:
        print("Err (likely ratelimit) | Use proxies | https://t.me/x6out")
    else:
      proxies = {
        'http': f"{prx}",
        'https': f"{prx}"
      }
      response = requests.post(url, json=payload, headers=headers, proxies=proxies)
      if response.status_code == 200:
        p = response.json()['token']
        pr = f"https://discord.com/billing/promotions/partner-promotions/1180231712274387115/{p}"
        with open("promos.txt", "a") as file:
          file.write(pr + "\n")
      else:
        print("Err | Check your proxies | https://t.me/x6out")

thread_list = []
for i in range(threads):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)
    thread.start()