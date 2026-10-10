from alerts.malware import MalwareAlert
from alerts.login import LoginAlert

alert = [LoginAlert("A002","HIGH","192.168.1.101","NEW",5),MalwareAlert("A003","CRITICAL","192.168.1.102","NEW","Ransomware")]

print("========= SOC ALERT MANAGER =========")
alert[0].display_alert()
alert[0].investigation()

print("\n---------------------------------------\n")
alert[1].display_alert()
alert[1].investigation()
   

# Alert ID: A001
# Severity: HIGH
# Source IP: 192.168.1.100

# Investigating 5 failed login attempts.

# ---------------------------------------

# Alert ID: A002
# Severity: CRITICAL
# Source IP: 192.168.1.101

# Investigating suspicious malware process.