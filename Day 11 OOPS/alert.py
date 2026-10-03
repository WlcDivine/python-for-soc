class alert:
     pass


alert1 = alert()
alert2=alert()




alert1.source_ip ='130.234.34.3'
alert1.username ='aman'
alert1.severnity = 'High'

alert2.source_ip ='234.54.14.67'
alert2.username = 'Raman'
alert2.severnity = "Low"

print("Alert 1 :")
print(alert1.source_ip)
print(alert1.username)
print(alert1.severnity)

print("Alert 2 :")
print(alert2.source_ip)
print(alert2.username)
print(alert2.severnity)