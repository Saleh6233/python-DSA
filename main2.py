
# if practicing
# is_magician = input("Are you a magician?")
# is_expert = input("Are you an expert in magic field?")
# if is_magician and is_expert:
#     print("You are a master magician!")
# elif is_expert or is_magician:
#     print("At least you're getting there!")
# else:
#     print("You need mana o_ _o")

# iterate dictionary
# player1 = {
#     'name': "Sibgut",
#     'age': 19,
#     'armor': "Basic Suit",
# }
# for field, status in player1.items():
#     print(field, status)
# for field in player1.keys():
#     print(field)
# for status in player1.values():
#     print(status)

# in range
# for num in range(0, 10, 3):
#     print("I am _____--_____")

# Enumerate
# for i, char in enumerate(list(range(40, 100, 2))):
#     if char == 50:
#         print(f"The index of {char} is: {i}")
#         break

# checking duplicates
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# myset = set()
# for item in some_list:
#     if some_list.count(item) > 1:
#         myset.add(item)
# print(myset)

# def checkEmptyString(field=None):
#     '''
#     Check if 'field' is emty
#     '''

#     if field is None:
#         print("Please fill the field")
#         return False
#     elif field == "":
#         print("Please fill the field")
#         return False
#     else:
#         return True
# i = 10
# while (i > 0):
#     name = input("Please enter your name: ")
#     if checkEmptyString(name):
#         break
# print(f"Your name is {name} ")

# def highest_even(my_list):
#     '''
#     Detects highest event number and returns it
#     '''
#     highest = 0
#     for item in my_list:
#         if item % 2 == 0:
#             if highest < item:
#                 highest = item

#     return highest


# print(highest_even([10, 2, 20, 48,  3, 4, 8, 11]))
