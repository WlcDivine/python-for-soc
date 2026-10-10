from alert import Alert
from manger import AlertManager

manager = AlertManager()

alert1 = Alert(101, "Failed Login", "HIGH")
alert2 = Alert(102, "Suspicious PowerShell", "CRITICAL")

manager.add_alert(alert1)
manager.add_alert(alert2)

print("ALL ALERTS")
manager.display_all()

print("\nUPDATING ALERT 101")
manager.update_alert(101, "CLOSED")

print("\nUPDATED ALERTS")
manager.display_all()

print("\nCRITICAL ALERTS")
manager.filter_by_severity("CRITICAL")
