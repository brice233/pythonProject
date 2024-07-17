# # exmple let writer
# # name: brice
# # age: 2
# # email: nd@gmail.com
# #  Remember  we can not duplicate it
# customer = {
#     "name": "brice",
#     "age": 2 ,
#     "is_verified":True
# }
# print(customer["name"]) #to have access on the key
#  # but instead of doing that  you do this.
#
# customer = {
#     "name": "brice",
#     "age": 2 ,
#     "is_verified":True
# }
# print(customer.get("name")) #this is much better than that above
#
# ###################################################################
# customer = {
#     "name": "brice",
#     "age": 2 ,
#     "is_verified":True
# }
# print(customer.get("birthdate","jan 1 1999"))
#
# ############################################## update something:
# customer = {
#     "name": "brice",
#     "age": 2 ,
#     "is_verified":True
# }
# customer["name"] = "jack"
# print(customer["name"])
# ############################################# add a new key:
# customer = {
#     "name": "brice",
#     "age": 2 ,
#     "is_verified":True
# }
# customer["birthday"] = "jan 1 1999"
# print(customer["birthday"])
##################################################################################
phone = input('phone: ')
mapping_dictionary ={
    "1":"one",
    "2":"two",
    "4":"four"
}
output = ""
for ch in phone:
    output += mapping_dictionary.get(ch, "!") + " "
    print(output)


