new = [{"user": "admin", "severity": 9},
    {"user": "alice", "severity": 3},
    {"user": "bob", "severity": 8}]
sort = sorted(new,key= lambda alert:alert["severity"] ,reverse=True)
print(sort)