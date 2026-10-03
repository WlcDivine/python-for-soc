def num():
    yield 1
    yield 2
    yield 3
a = num()
print(next(a))
print(next(a))

# also 
for num in num():
    print(num)