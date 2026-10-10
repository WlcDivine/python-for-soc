

from alert import Alert
# Alert manager
class AlertManager:


    def __init__(self):
        self.alerts = []


    def add_alert(self,alert):
        self.alerts.append(alert)


    def display_all(self):
      
        for alert in self.alerts:
            # create a alert list 
         for alert in self.alerts: 
            alert.display() 
            print("-" * 30)


    def update_alert(self, alert_id, new_status):
        for alert in self.alerts:
             if alert.alert_id == alert_id: alert.update_status(new_status) 
             return True
        return False

    
    def filter_by_severity(self, severity): 
        for alert in self.alerts: 
            if alert.severity.upper() == severity.upper(): alert.display() 
            print("-" * 30)