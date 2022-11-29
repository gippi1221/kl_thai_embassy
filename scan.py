import requests
import time
from datetime import datetime
import json
import os
import sys

def send_to_telegram(message):
  apiToken = os.environ['TG_API_TOKEN']
  chatID = os.environ['TG_CHAT_ID']
  apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
  try:
    response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
    print(datetime.now().strftime('%m/%d/%Y, %H:%M:%S') + ' ' + response.text)
  except Exception as e:
    print(datetime.now().strftime('%m/%d/%Y, %H:%M:%S') + ' ' + e)


s = os.environ['API_LINK']

print(datetime.now().strftime('%m/%d/%Y, %H:%M:%S') + ' starting...')

while (True):
  x = requests.get(s)
  data = json.loads(x.content)

  if len(data) > 0:
    send_to_telegram(';'.join(data))
    time.sleep(30)

  time.sleep(2)
