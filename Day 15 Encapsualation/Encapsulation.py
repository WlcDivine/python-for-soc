class alert:

    def __init__(self, severity):
        self._severity = severity

    def update_severity(self, new_severity):

        allowed = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

        if new_severity in allowed:
            self._severity = new_severity
        else:
            print("Invalid severity")

    def display(self):
        print("Severity:", self._severity)

alert1 = alert("Low")

alert1.display()

alert1.update_severity("MEDIUM")
alert1.display()


    
