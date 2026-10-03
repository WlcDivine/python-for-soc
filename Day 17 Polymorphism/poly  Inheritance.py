
class Login_Alert():
       def respond(self):
            print("Investiagation is working")

class malwareAlert():
     def respond(self):
          print("Isolated affected system")

class network:
      def respond(self):
            print("the network traffic is very high ")
      

alerts = [Login_Alert(),
          malwareAlert(),
          network()]
for alert in alerts:
      alert.respond()