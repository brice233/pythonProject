name = ['brice', 'bebe','eden','jabo']
print(name)
######or
name = ['brice', 'bebe','eden','jabo']
print(name[2])
######or
name = ['brice', 'bebe','eden','jabo']
print(name[-1])
######or
name = ['brice', 'bebe','eden','jabo']
print(name[2:])
######or
name = ['brice', 'bebe','eden','jabo']
print(name[0:2])
######or
name = ['brice', 'bebe','eden','jabo']
name[0] ='maman'
print(name)

# challenge 1: write a program to find largest numbers in list
numbers = [3,6,2,8,4,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
