# task 1
sq = lambda x:x*x
print(sq(5))

# task 2
users = [" admin ", " alice ", " bob "]
new_user = list(map(lambda user: user.strip(),users))
print(new_user)

# task 3 
failed_attempts = [2, 8, 1, 12, 5, 3]
filters = list( filter (
    lambda ch : ch>=5,
    failed_attempts
))
print(filters)
# task 4
alerts = [
    {"user": "admin", "severity": 9},
    {"user": "alice", "severity": 3},
    {"user": "bob", "severity": 8},
    {"user": "root", "severity": 10}
]
sorting = sorted(alerts, key =lambda alert:alert["severity"],reverse=True)
print(sorting)