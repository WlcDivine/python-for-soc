def func(x):
    return x*x
print(func(5))

#lambda to print square
square = lambda x:x*x
print("square using lambda:",square(9))
# use for only small function 

servinty = lambda c: "High" if c>=8 else "LOW"
print(servinty(11))