#  day 8 1-b 2-b 3-b 4-b 5-it provide a output in a tuple 

from datetime import datetime
now  = datetime.now()
print(now)

print(now.strftime("%Y-%m-%d %H:%M:%S"))

timestamp = "2026-09-06 13:20:35"
covert_date =datetime.strptime(timestamp,"%Y-%m-%d %H:%M:%S")
print("coverted date:",covert_date)

login1 = datetime.strptime("2026-09-13 10:00:00", "%Y-%m-%d %H:%M:%S")
login2 = datetime.strptime("2026-09-13 10:07:45", "%Y-%m-%d %H:%M:%S")
print("time difference :",(login2-login1).seconds)