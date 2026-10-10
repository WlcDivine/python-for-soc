with open("Security.log", "a") as file:

# create and update the security  log file 
    file.write("FAILED LOGIN - 192.168.1.10\n")
    file.write("SUCCESS LOGIN - 192.168.1.20\n")
    file.write("FAILED LOGIN - 192.168.1.10\n")

print("Security Log successfully updated!")

# print the data of the security log file
with open("Security.log", "r") as file:
    data = file.read()
    print(data)

failed_count = 0 

with open("Security.log","r") as file:
    for line in file:
        if "FAILED LOGIN" in line:
            failed_count += 1
print(f"Total failed login attempts: {failed_count}")

# new event append to the security log file
with open("Security.log","a") as file:
    file.write("FAILED LOGIN - 192.168.1.30\n")
print("new event append")
