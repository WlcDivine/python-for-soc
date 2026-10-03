from datetime import datetime

# task 1 
now = datetime.now()
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

# task 2
date ="2026-12-25 23:45:30"
date_object = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
print("Date yrs:", date_object.year,"hour:",date_object.hour,"min:",date_object.minute,)

# task 3
login_times = [
    "2026-09-06 08:30:00",
    "2026-09-06 10:15:00",
    "2026-09-06 13:45:00",
    "2026-09-06 22:30:00",
    "2026-09-06 03:20:00"
]

for login_time in login_times:
    hour = datetime.strptime(login_time, "%Y-%m-%d %H:%M:%S").hour
    if hour < 9 or hour > 18:
        print(f"Suspicious login time: {login_time}")
    else:
        print(f"Normal login time: {login_time}")

# task 4
login1 =datetime.strptime("2026-09-06 10:00:00","%Y-%m-%d %H:%M:%S")
login2 =datetime.strptime("2026-09-06 10:02:30","%Y-%m-%d %H:%M:%S")
diff = login2 - login1
print("Time difference:", diff.seconds)