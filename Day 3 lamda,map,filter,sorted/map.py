scores = [1,2,3,4,5,6]
newscore =[]
for a in scores :
    newscore.append(a*10)
print(newscore)

# using map 
new_scores = list(map(lambda x: x * 10, scores))

print(new_scores)

ips = [
    " 192.168.1.10 ",
    " 10.0.0.5 ",
    " 8.8.8.8 "
]
clean = list(map(lambda ip: ip.strip(),ips))
print(clean)