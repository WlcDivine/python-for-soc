def show_alert(*alerts):
    for alert in alerts:
      print("alert:-",alert)
show_alert("malware","port scan","brute force")

# task 2

def alert(**detail):
   for i in detail:
     print(i,":",detail[i])
alert(user="admin",ip="10.0.0.5",severity="HIGH")

# task 3
'''*agrs are the help to call multiple value in a single parameter throught a function in a form of 
tuples, **keyargs  call the value of the throught function in a dict format it can call multiple value 
in a key value method
'''