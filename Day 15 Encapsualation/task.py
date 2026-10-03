class alert:
    def __init__(self,alert_id ,username ,severity):
        self.alert_id= alert_id
        self.useraneme= username
        self._severity= severity

    def get_severity(self):
        return self._severity
    def update_severity(self,new_severity):
        li = ["Low","High","Medium","Extreme"]
        if new_severity  in li :
            self._severity = new_severity
        else :
            print("Invalid choice ")

alert1 = alert("A001","admin","Low")
print(alert1.get_severity())
alert1.update_severity("Medium")
print(alert1.get_severity())
alert1.update_severity("High")

print(alert1.get_severity())
alert1.update_severity("Extreme")
print(alert1.get_severity())
alert1.update_severity("Banana")
print(alert1.get_severity())