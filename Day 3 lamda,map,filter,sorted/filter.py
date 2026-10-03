alerts = [
    {"user": "admin", "severity": 9},
    {"user": "alice", "severity": 3},
    {"user": "bob", "severity": 8}
]
check =[alert
         for alert in alerts 
         if alert["severity"]>4
]
print(check)

# using filter 
high_alert = list(filter(
    lambda ch:ch["severity"]>8
    ,alerts
))
print(high_alert)
