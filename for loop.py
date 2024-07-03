# use it to iterate over item of a colletions
# such as string . because string is sequencw  of character
#
# example 1:
for item in 'python':
    print(item)

# example 2: here on list
for item in ['brice','john','sarah']:
    print(item)

# example 3:
for item in range(10):
    print(item)
# N.B: 10 is not included. so basically we call range function,this range create on object
# it not list , its special kind of object we can iterate over.

prices = [10,20,30]
total = 0
for price in prices:
      total += price
print(f"total: {total}")



