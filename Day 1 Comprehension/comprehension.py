ips = [
    "192.168.1.10",
    "8.8.8.8",
    "10.0.0.5",
    "185.22.34.91",
    "192.168.1.20"
]
failed_ips =[ip for ip in ips if ip.startswith("192.169")]
print(failed_ips)

# list conmprehension 
num = [1,2,3,4,5,6]
num_Square =[nums*nums  for nums in num  ]
print("numbers",num,"their squares",num_Square)

# dictionary
users = {
    "admin",
    "alice",
    "bob"
}
user_len = {user: len(user) for user in users}
print(user_len)

