import requests
import time
from datetime import datetime, date, timedelta
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

#getting start of period
today = date.today()
curr_year = today.strftime("%Y")
curr_month = today.strftime("%m")
first_day = datetime(int(curr_year), int(curr_month), 1)

prev_sun = first_day
if (first_day.weekday() != 7):
  idx = (first_day.weekday() + 1) % 7
  prev_sun = first_day - timedelta(idx)

start_year = prev_sun.strftime("%Y")
start_month = prev_sun.strftime("%m")
start_day = prev_sun.strftime("%d")

#TODO: get the same for the end of period
#it's quite unpredictable now, so we have to wait next year :)

s = f'https://my.linistry.com/api/CustomerApi/GetAvailabilityAsync?serviceId=3fb796f6-3829-40b9-a549-3feb2b12453a&startyear={start_year}&startmonth={start_month}&startday={start_day}&endyear=2022&endmonth=12&endday=31&count=1'

print(datetime.now().strftime('%m/%d/%Y, %H:%M:%S') + ' starting...')

while (True):
  x = requests.get(s)
  data = json.loads(x.content)

  if len(data) > 0:
    send_to_telegram(';'.join(data))
    time.sleep(30)

  time.sleep(2)
