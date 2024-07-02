# if temperature is greater than 30
#     it's hot day
# otherwise if it's less than 10
#     it's cold day
# otherwise
# it's neither cold nor hot

temperature = 12
if temperature >30:
    print("it's hot day")
elif temperature <= 10:
    print("it's cold day")
else:
    print("it's neither cold nor hot")

####################
# if name is less than 3 characters long
#     name must be at least 3 characters
# otherwise if it's more than 50 characters
#      name can be maximun of 50 charaters
# otherwise
#       name look good

name = "john smith"
if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name) > 50:
    print("name can be maximun of 50 charaters")
else:
    print("name look good")
