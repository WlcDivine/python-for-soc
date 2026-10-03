iterator =["sam","bob","alice"]
# contain multiple data called as iterator
user_iterator = iter(iterator)
print(next(user_iterator))
print(next(user_iterator))
print(next(user_iterator))
print(next(user_iterator)) # gives an error 