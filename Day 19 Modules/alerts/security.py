class SecurityAlert:

    def __init__(self, alert_id, severity, source_ip, status):
        self.alert_id = alert_id
        self.severity = severity
        self.source_ip = source_ip
        self.status = status

    def display_alert(self):
        print(f"Alert ID: {self.alert_id}")
        print(f"Severity: {self.severity}")
        print(f"Source IP: {self.source_ip}")
        print(f"Status: {self.status}")

    def update_status(self, new_status):
        self.status = new_status
        print(f"Alert updated to {self.status}")