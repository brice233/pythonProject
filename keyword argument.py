def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('welcome aboard')

print("start")
greet_user("john",last_name="smith")
print ("finish")
#NB. For most part use position arguments if you're dealing with function that take multiple
#numerical value & it's not quite clear what those value represent, use keyword arguments to
# improve the readability of your code, and finally if your passing both positons and keyword argument
# use the keyword argument after the position argument.