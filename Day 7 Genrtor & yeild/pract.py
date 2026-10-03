def alerts():
    yield "LOW"
    yield "MEDIUM"
    yield "HIGH"
for num in alerts():
    print(num)
# pract 2
def num():
    for i in range(1,11):
       yield i
for num in num():
    print(num)

#pract 3
def process_logs(filename):
    with open(filename, "r") as file:
         for lines in file:
             yield lines.strip()

for line in process_logs("auth.log"):
    print(line)