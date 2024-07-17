def greet_user(name):
    print(f'Hi {name} there!')
    print('welcome aboard')

print("start")
greet_user("john")
print ("finish")

###########################when never we define a parameter for our functoin  we should alway supply
# look this example here to explain it well.

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('welcome aboard')

print("start")
greet_user()
print ("finish")