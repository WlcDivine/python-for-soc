class alert :
    # class atribute
    organization = "CyberSOC"

    #  instance attribute
    def __init__(self,alert_id,username,severity,status):
        self.alert_id = alert_id
        self.username = username 
        self.severity = severity
        self.status = status

        
alert1 = alert("A001","admin","HIGH","open")
alert2 = alert("A002","jetaleli","low","open")

print(f" Alert :\n {alert1.alert_id}\n {alert1.username}\n {alert1.severity}\n {alert1.status}\n {alert1.organization}")
print(f" Alert :\n {alert2.alert_id}\n {alert2.username}\n {alert2.severity}\n {alert2.status}\n {alert2.organization}")

# task 3 
class new :
    alert_type = "Authentication"
    def __init__(self,username,severity):
        self.username =username
        self.severity = severity 

new1 = new("hans newman","Low")
new2 = new("Vishy Anand ","Medium")
new3 = new("Garry kasparov","High")
# alert_ type is class brcsause for diiferent object the alert_type will call automatically the actual value 
# but in username is instance method because for different object the username will be different so it is instance method

print(f" Alert :\n {new2.username}\n {new2.severity}\n {new2.alert_type}")

print(f" Alert :\n {new3.username}\n {new3.severity}\n {new3.alert_type}")
