# alert class 
class Alert:

    def __init__(self,alert_id,event,severity,):
        self.alert_id = alert_id
        self.event = event
        self.severity = severity
        self.status = "open"

# display
    def display(self):

        print(f"Alert Id :{self.alert_id} \nevent :{self.event} \nseverity :{self.severity} \nstatus :{self.status}")
#update alert 
    def update_status(self,new_status):
        self.status = new_status
        

