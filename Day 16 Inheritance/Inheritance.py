class Alert :
    def display(self):
        print("We display the data here ")

class NewAlert(Alert):
    pass 
alert1 = NewAlert()
alert1.display()

