with open("security.log","r") as file:
    for line in file :
        print(line.strip())

failed =0
with open("security.log","r") as file:
    for line in file :
        if "FAILED LOGIN" in line :
            failed +=1
print("Failed login :",failed)


