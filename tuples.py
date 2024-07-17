# so similiar to lists you address individual items using using square blackets
numbers = (1,2,3)
print(numbers[0])

# NB. if you try to change the first item you will get an error like example here under:
numbers = (1,2,3)
numbers[0]= 10 #this is an error bcz tuple object doesn't support item assignment.so we can not mutate or change it
print(numbers[0])