# ========== SOC LOG REPORT ==========

# Total Events: 8
# Failed Logins: 5
# Successful Logins: 3

# Top Source IPs:
# 192.168.1.10 → 4 events
# 10.0.0.5 → 2 events

# Usernames:
# admin → 5 events
# alice → 3 events

logs = [
    "2026-09-13 10:00:00,admin,192.168.1.10,FAILED_LOGIN",
    "2026-09-13 10:01:00,admin,192.168.1.10,FAILED_LOGIN",
    "2026-09-13 10:02:00,alice,10.0.0.5,SUCCESS_LOGIN",
    "2026-09-13 10:03:00,admin,192.168.1.10,FAILED_LOGIN",
    "2026-09-13 10:04:00,bob,192.168.1.20,SUCCESS_LOGIN",
    "2026-09-13 10:05:00,alice,10.0.0.5,FAILED_LOGIN",
    "2026-09-13 10:06:00,admin,192.168.1.10,FAILED_LOGIN",
    "2026-09-13 10:07:00,bob,192.168.1.20,SUCCESS_LOGIN",
    "2026-09-13 10:08:00,admin,192.168.1.10,FAILED_LOGIN",
    "2026-09-13 10:09:00,admin,192.168.1.10,FAILED_LOGIN"
]
Total_count = len(logs)
Failed_logins = 0
Successful_logins = 0
Source_ip_count = {}
Usernames = {}

for log in logs:
    event_type =log.split(",")[3]
    source_ip = log.split(",")[2]   
    username = log.split(",")[1]
    if username in Usernames:
        Usernames[username] += 1
    else:
        Usernames[username] = 1
    if source_ip in Source_ip_count:
        Source_ip_count[source_ip] += 1
    else:
        Source_ip_count[source_ip] = 1

    if event_type == "FAILED_LOGIN":
        Failed_logins += 1
    elif event_type == "SUCCESS_LOGIN":
        Successful_logins += 1

print(f"Total Events: {Total_count}")
print(f"Failed Logins: {Failed_logins}")
print(f"Successful Logins: {Successful_logins}")

print("\nTop Source IPs:")
for ip, count in sorted(Source_ip_count.items(), key=lambda x: x[1], reverse=True) :
    print(f" {ip} → {count} events")

print("\nUsernames:")
for username, count in Usernames.items():
    print(f" {username} → {count} events")