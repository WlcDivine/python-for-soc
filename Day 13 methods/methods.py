class alert :
    def display(self):
        print("Alert: This is a notification message.")
alert1 = alert()
alert1.display()
class Alert:

    def __init__(self, alert_id, username,status):
        self.alert_id = alert_id
        self.username = username
        self.status = status

    def display(self):
        print("Alert ID:", self.alert_id)
        print("Username:", self.username)
        print("Status:", self.status ,"\n")


    def update(self, new_status):
        self.status = new_status

       

alert1 = Alert("A001", "admin","open")

alert1.display()
alert1.status = "investigation"
alert1.display()