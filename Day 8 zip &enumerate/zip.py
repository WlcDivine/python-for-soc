users = ["admin", "alice", "bob"]
ips = ["192.168.1.10", "192.168.1.20", "192.168.1.30"]
# add the two list 

for user, ip in zip(users, ips):
    print(user, ip)


names = ["A", "B", "C"]
# enumerate helps to get the index  and iterate 
for i, name in enumerate(names, start=1):
    print(i, name)