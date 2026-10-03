# task 1 
user = ["admin","alice","bob","root"]
iterator = iter(user)
print(next(iterator))
print(next(iterator))

# task 2 
alerts = [
    "LOW: Failed login",
    "MEDIUM: Multiple failed logins",
    "HIGH: Suspicious process"
]
user = iter(alerts)
print("first alert :-",next(user))
print("second alert :-",next(user))
print("third alert :-",next(user))

# task 3
ips =["192.168.1.10", "10.0.0.5"]
ip = iter(ips)
while True:
    try:
        cp = next(ip)
        print(cp)
    except StopIteration:
        break 
# task 4
event_army = [
    "FAILED LOGIN admin",
    "SUCCESS LOGIN alice",
    "FAILED LOGIN root"
]
Ds = iter(event_army)
failed_count=0
Sucess_count=0
while True:
    try:
        cd = next(Ds)
        if cd.startswith("FAILED"):
            failed_count+=1
        if cd.startswith("SUCCESS"):
                    Sucess_count+=1    
    except StopIteration:
        break 
print(failed_count)
print(Sucess_count)