# normal call 
def greet(user):
    print("Hello User:",user)
greet("divine")

# using args we call more than one value through one parameter
def new_alert(*name):
    print("hello user ",name)

new_alert("divine")
new_alert("adam","jack","oggy","bob")
# also we can any argument through this 

# in the name is work as tuple

a={
    "name":"harry",
    "rollno":3
}
li= [1,2,3,4,5]
new_alert(a,li)