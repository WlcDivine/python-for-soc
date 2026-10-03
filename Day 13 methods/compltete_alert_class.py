class Alert :
    def __init__(self, alert_id, username,severity,status):
        self.alert_id = alert_id
        self.username = username
        self.severity = severity
        self.status = status 


    def display(self):
        print("Alert ID " ,self.alert_id )
        print("Username ",self.username)
        print("Severity ",self.severity)
        print("Status ", self.status )
        print()


    def update(self, new_status):
        self.status = new_status

    def escalate(self):
        self.severity = "High"

alert2 =Alert("A002","user1","Low","open")
alert1 = Alert("A001","admin ","Medium","open")
alert2.display()
alert1.display()


alert1.update("investigation")
alert1.escalate()
alert1.display()
alert2.display()