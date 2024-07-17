numbers = [1,2,3,4,5,6,7]
numbers.append(12) # it's for add new number on the list
print(numbers)

################### second
numbers = [1,2,3,4,5,6,7]
numbers.append(0,10) # it's for add new number in middle or at the begining of our list
print(numbers)

################# Third
numbers = [1,2,3,4,5,6,7]
numbers.remove(5) # we also remove a number
print(numbers)

############# fouth
numbers = [1,2,3,4,5,6,7]
numbers.clear() # if clean all in the list
print(numbers)

############## fifth
numbers = [1,2,3,4,5,6,7]
numbers.pop() #  we can remove last number on our list
print(numbers)

############# six
numbers = [1,2,3,4,5,6,7]
print(numbers.index(1)) # if wanna know the existence
###### other way and which is a better one is
numbers = [1,2,3,4,5,6,7]
print(50 in numbers)

########### seventheen
numbers = [1,2,3,4,5,6,7]
numbers.sort() #  the put them in order but ascending order
numbers.reverse() # put descending order if you want
print(numbers)

# the last one is the copy method with this method can get copy of our list
numbers = [1,2,3,4,5,6,7]
numbers2 = numbers.copy()#now number2,is copy of our original list.if any change on it.not impact on the second list.
numbers.append(10)#let add item ten.so the first number  is updated we hve new item on our list only first list
print(numbers2)# if print it. we don't have the number10. because these are two independent list.

# challenge on this
# write a program to remove the duplicate in a list
numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
