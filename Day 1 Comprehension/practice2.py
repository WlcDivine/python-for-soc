events = [
    {"user": "admin", "status": "FAILED"},
    {"user": "alice", "status": "SUCCESS"},
    {"user": "bob", "status": "FAILED"},
    {"user": "admin", "status": "FAILED"},
    {"user": "john", "status": "SUCCESS"}
]

failed_events = [
    event for event in events
    if event["status"] == "FAILED"
]

failed_users = {
    event["user"] for event in events
    if event["status"] == "FAILED"
}

print(failed_events)
print(failed_users)