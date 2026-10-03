# task 1
with open("auth.log","r") as file :
    n=1
    for line in file :
        print("Event no",n,": ",line.strip())
        n+=1
# task 2 
print("task")
count =0
success =0
failed =0
with open("auth.log","r") as file:
  
    for line in file:
        l= line.strip()
        if "FAILED LOGIN" in l :
            count+=1
            failed+=1
        elif "SUCCESS LOGIN" in l :
            count+=1
            success+=1
print("Total event",count)
print("Succesfull login",success)
print("Failed login ",failed)

# task 3 
with open("auth.log", "r") as file:
    for line in file:
        line = line.strip()

        if "FAILED LOGIN" in line:
            parts = line.split()

            for part in parts:
                if part.startswith("ip="):
                    ip = part.split("=")[1]
                    print(ip)

# bonus 
ip_count = {}

with open("auth.log", "r") as file:
    for line in file:
        line = line.strip()

        if "FAILED LOGIN" in line:
            parts = line.split()

            for part in parts:
                if part.startswith("ip="):
                    ip = part.split("=")[1]

                    if ip in ip_count:
                        ip_count[ip] += 1
                    else:
                        ip_count[ip] = 1

print(ip_count)