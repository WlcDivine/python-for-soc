from .security import SecurityAlert


class LoginAlert(SecurityAlert):
       def __init__(self,alert_id,severity,source_ip,status,failedAttempts):
           super().__init__(alert_id,severity,source_ip,status)
           self.failedAttempts = failedAttempts

       def investigation(self):
            print(f"Investigating login alert {self.alert_id} from IP {self.source_ip} with {self.failedAttempts} failed attempts.")

alert =LoginAlert("A001", "High", "192.168.1.100", "New", 5)

alert.display_alert()
alert.investigation()
alert.update_status("Investigated")
print("\n")

