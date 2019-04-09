import datetime
import time

time_now = datetime.datetime.now()

delta = int(input("Enter time delta in seconds between 10 and 20 seconds :"))
if 10 < delta < 20:
  print("Current time is ",time_now)
  endtime = time_now+datetime.timedelta(seconds=delta)
  time.sleep(delta/2)
  print("Half time : beep")
  time.sleep(delta/2)
  print("Full Time : beep") 
else:
  print("invalid Entry")
  
