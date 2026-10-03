login_count ={
    "aman":433,
    "ayush":12,
    "bob":3,
    "root":34
}
suspicious = {user:count
               for user,count in login_count.items()
               if count >10
    }
print(suspicious)

#  sets 
logs = [
    "192.168.1.10",
    "8.8.8.8",
    "192.168.1.10",
    "8.8.8.8",
    "1.1.1.1"
]
unique_ips = {ip for ip in logs}
print(unique_ips)