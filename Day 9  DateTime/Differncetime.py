from datetime import datetime
login1 =datetime.strptime("2026-09-06 10:00:00","%Y-%m-%d %H:%M:%S")
login2 = datetime.strptime("2026-09-06 10:05:00","%Y-%m-%d %H:%M:%S")
time_diff = login2 - login1
print("Time difference:", time_diff)
print("in sec",time_diff.total_seconds())

login_time = datetime.strptime(
    "2026-09-06 04:30:00",
    "%Y-%m-%d %H:%M:%S"
)
hour =login_time.hour
if hour <9 or hour >13:
    print("suspicous login time")
else :
    print("normal login time")
