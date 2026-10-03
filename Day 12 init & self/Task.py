class  User:
    def __init__(self, name, role):
        self.name = name 
        self.role =role
User1 =User("John Doe", "Admin")
print(User1.name)
print(User1.role)
# Task 2
class alert :
    def __init__(self,source_ip,username,attack_type,severity):
        self.source_ip = source_ip
        self.username = username
        self.attack_type = attack_type
        self.severity = severity

alert1 =alert("192.168.1.10", "alice", "SQL Injection", "High")
alert2 =alert("234,34,21,2", "bob", "Cross-Site Scripting", "Medium")
alert3 =alert("44.34.21.66", "charlie", "Denial of Service", "Critical")
l1= [alert1, alert2, alert3]
for i in range(1,4):
    print("Alert", i)
    print("IP",l1[i-1].source_ip)
    print("Username",l1[i-1].username)
    print("Attack Type",l1[i-1].attack_type)
    print("Severity",l1[i-1].severity)
    print()

# self is a function use to call the variable of the class and it is used to access the variable of the class it is a reference to the current instance of the clas

# task 4= missing using of self in the class to fix this use self to intiate a variable   eg self.username =username

class check :
    def __init__(self,source_ip,username,severnity,status):
        self.source_ip = source_ip
        self.username = username
        self.severnity = severnity
        self.status = status
check1=check("192.168.1.10", "alice", "High", "Open")
check2=check("192.168.1.11", "bob", "Medium", "In Progress")
check3=check("192.168.1.12", "charlie", "Critical", "Closed")
checkn= [check1, check2, check3]
for i in range(1,4):
    if checkn[i-1].severnity == "High":
        print("Alert", i)
        print("IP",checkn[i-1].source_ip)
        print("Username",checkn[i-1].username)
        print("Severity",checkn[i-1].severnity)
        print("Status",checkn[i-1].status)
        print()
