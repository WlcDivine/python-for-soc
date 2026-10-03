def read_log(fileName):
    with open(fileName,'r') as file:
          for line in file:
               yield line.strip()


# read line
for log in read_log("auth.log"):
     print(log) 


# list append
def get_logs():
    logs = []

    for i in range(1000000):
        logs.append(i)

    return logs

def get_logs():
    for i in range(1000000):
        yield i


# genrator
def failed_logins(filename):
    with open(filename, "r") as file:
        for line in file:
            if "FAILED LOGIN" in line:
                yield line.strip()
for d in failed_logins("auth.log"):
    print("*",d)