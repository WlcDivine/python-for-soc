class SecurityAlert:
    def __init__(self,alert_id,severity,source_ip,status):
        self.alert_id = alert_id
        self.severity = severity
        self.source_ip= source_ip
        self.status = status

    def Display_Alert(self):
        print(f"Alert ID: {self.alert_id},\n Severity: {self.severity},\n Source IP: {self.source_ip},\n Status: {self.status}")
    def update_status(self,new_status):
        self.status = new_status
        print(f"Alert {self.alert_id} status updated to {self.status}.")
        

# child class 
class LoginAlert(SecurityAlert):
       def __init__(self,alert_id,severity,source_ip,status,failedAttempts):
           super().__init__(alert_id,severity,source_ip,status)
           self.failedAttempts = failedAttempts

       def investigation(self):
            print(f"Investigating login alert {self.alert_id} from IP {self.source_ip} with {self.failedAttempts} failed attempts.")
    
class MalwareAlert(SecurityAlert):
     def __init__(self, alert_id, severity, source_ip, status,processName):
        super().__init__(alert_id, severity, source_ip, status)
        self.processName = processName

     def investigation(self):
        print(f"Investigating malware alert {self.alert_id} from IP {self.source_ip} related to process {self.processName}.")



class  NetworkAlert(SecurityAlert):
       def __init__(self, alert_id, severity, source_ip, status,destination_port):
           super().__init__(alert_id, severity, source_ip, status)
           self.destination_port =  destination_port

       def investigation(self):
            print(f"Investigating network alert {self.alert_id} from IP {self.source_ip} targeting port {self.destination_port}.")


class PhishingAlert(SecurityAlert):
       def __init__(self, alert_id, severity, source_ip, status,email_sender):
            super().__init__(alert_id, severity, source_ip, status)
            self.email_sender = email_sender

       def investigation(self):
            print(f"Investigating phishing alert {self.alert_id} from IP {self.source_ip} sent by {self.email_sender}.")


alerts = [LoginAlert("A001", "High", "192.168.1.100", "New", 5), 
          MalwareAlert("A002", "Critical", "192.168.1.101", "New", "SuspiciousProcess"),
          NetworkAlert("A003", "Medium", "192.168.1.102", "New", 80),
          PhishingAlert("A004", "High", "192.168.1.103", "New", "spam@gamil.com")]
for alert in alerts:
    alert.Display_Alert()
    alert.investigation()
    alert.update_status("Investigated")
    print("\n")

