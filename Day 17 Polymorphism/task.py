class SecurityAlert():
    def respond(self):
        print("Investigating security alert")
class LoginAlert(SecurityAlert):
    def respond(self):
        print("Investigating suspicious login")

class MalwareAlert(SecurityAlert):
    def respond(self):
        print("Investigating  malware activity")

class NetworkAlert(SecurityAlert):
    def respond(self):
        print("Investigating network activity")
li = [LoginAlert(),MalwareAlert(),NetworkAlert()]
for alert in li:
    alert.respond()

# task 2 
class SecurityAlert1():
    def display(self):
        print("Investigating security alert")

class BruteForceAlert(SecurityAlert1):
    def display(self):
        print("[BRUTE FORCE] Multiple failed login attempts detected")
class PortScanAlert(SecurityAlert1):
    def display(self):
        print("[PORT SCAN] Multiple ports contacted by one source")
class MalwareAlert(SecurityAlert1):
    def display(self):
        print("[MALWARE] Suspicious process detected")


# task 3
alerts = [
    BruteForceAlert(),
    MalwareAlert(),
    PortScanAlert(),
    BruteForceAlert()
]
for alert in alerts:
    alert.display()
