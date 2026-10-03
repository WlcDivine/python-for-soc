# first way 
file = open("harr.txt","r")
data = file.read()
print(data)
file.close()
# but if the error occur file will never be close so thier is a way


# second way 
with open("harr.txt","r") as file1:
    data = file1.read()
    print(data)

