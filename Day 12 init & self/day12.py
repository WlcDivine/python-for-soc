class alert :
    def __init__(self,source_ip,username,severnity):
        self.source_ip = source_ip
        self.username = username
        self.severnity = severnity 

alert1 = alert("245.54.34.54", "john_doe", "High")
alert2 = alert("10.0.0.5", "rahul", "Low")

print(alert1.source_ip)
print(alert1.username)
print(alert1.severnity)

print()

print(alert2.source_ip)
print(alert2.username)
print(alert2.severnity)



class new :
    def __init__(self):
        print("This is  a new class ")
new1= new()
        