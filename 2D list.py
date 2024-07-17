martix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(martix[0][1]) # to access the number

######### modify or replace number
martix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
martix [0] [1] = 20
print(martix[0][1])

########### we can also use nexted loop to iterate over all the item
# in this matrix
martix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in martix:
    for item in row:
        print(item)

