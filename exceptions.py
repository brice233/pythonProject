try:
    age = int(input('age: '))
    print(age)
except ValueError:
    print('invalid value')
###################################### now different kind of errors or exception
try:
    age = int(input('age: '))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('invalid value')