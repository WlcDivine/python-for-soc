class LoginAlert:
    def respond(self):
        print("Investigate Suspicipus login")

class Malware_Alert:
    def respond(self):
        print("Isolate infected system")

alert1 = LoginAlert()
alert2 = Malware_Alert()

alert1.respond()
alert2.respond()