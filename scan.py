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
def get_start_end_dates(dt):
  curr_year = dt.strftime("%Y")
  curr_month = dt.strftime("%m")
  first_day = datetime(int(curr_year), int(curr_month), 1)

  prev_sun = first_day
  if (first_day.weekday() != 7):
    idx = (first_day.weekday() + 1) % 7
    prev_sun = first_day - timedelta(idx)

  start_year = prev_sun.strftime("%Y")
  start_month = prev_sun.strftime("%m")
  start_day = prev_sun.strftime("%d")

  last_day = (dt.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)
  last_sun = last_day
  if (last_day.weekday() != 5):
    idx = (12 - last_sun.weekday()) % 7
    last_sun = last_sun + timedelta(idx)

  end_year = last_sun.strftime("%Y")
  end_month = last_sun.strftime("%m")
  end_day = last_sun.strftime("%d")

  return start_year, start_month, start_day, end_year, end_month, end_day

#current month
dt = date.today()
sy, sm, sd, ey, em, ed = get_start_end_dates(dt)
s1 = f'https://my.linistry.com/api/CustomerApi/GetAvailabilityAsync?serviceId=3fb796f6-3829-40b9-a549-3feb2b12453a&startyear={sy}&startmonth={sm}&startday={sd}&endyear={ey}&endmonth={em}&endday={ed}&count=1'

#next month
dt = (date.today().replace(day=1) + timedelta(days=32)).replace(day=1)
sy, sm, sd, ey, em, ed = get_start_end_dates(dt)
s2 = f'https://my.linistry.com/api/CustomerApi/GetAvailabilityAsync?serviceId=3fb796f6-3829-40b9-a549-3feb2b12453a&startyear={sy}&startmonth={sm}&startday={sd}&endyear={ey}&endmonth={em}&endday={ed}&count=1'

print(datetime.now().strftime('%m/%d/%Y, %H:%M:%S') + ' starting...')

while (True):
  x = requests.get(s1)
  data = json.loads(x.content)

  if len(data) > 0:
    send_to_telegram(';'.join(data))
    time.sleep(30)

  x = requests.get(s2)
  data = json.loads(x.content)

  if len(data) > 0:
    send_to_telegram(';'.join(data))
    time.sleep(30)

  time.sleep(2)
