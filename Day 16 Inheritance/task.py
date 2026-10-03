class Alert:
    def __init__(self,alert_id ,severity):
        self.alert_id = alert_id
        self.severity = severity
    def Display(self):
        print("Alert id :",self.alert_id)
        print("Severity :",self.severity)

class LoginAlert(Alert):
    def  __init__(self,alert_id,severity,username,source_ip):
        super().__init__(alert_id,severity)
        self.username = username
        self.source_ip = source_ip
    def Login_detail(self):
        print("Username :",self.username)
        print("IP address :",self.source_ip)
class MalwareAlert(Alert):
    def __init__(self,alert_id ,severity,process_name,file_Hash):
        super().__init__(self,alert_id,severity)
        self.process_name = process_name
        self.file_Hash = file_Hash

alert1=LoginAlert("A001","HIGH","admin","127.31.197.5")
alert1.Display()
alert1.Login_detail()

