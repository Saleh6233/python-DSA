# Fundamental Data Types
# print(type(2.89))
# print(f"2^4 =  {2 ** 3}")
# print(5 // 4)
# print(6 % 4)


# Operator Precedence
# print((20-3) + 2 ** 2)
####### 17 +  4     ################
# ()
# **
# */
# +-

# Variables
# a, b, c = 1, 2, 3
# print(f"{a} + {b}+  {c} = {a+b+c}")
# Statement               Expression

# str
# long_string = '''
# WOW
# O O
# ---
# '''
# print(long_string)
# print(" ^")
# print(" |")
# print("That's weird!")

# Escape Sequence
# price = input("Please enter your price?\n \t")
# quantity = input("Please enter quantity: \n \t")
# price = float(price)
# quantity = int(quantity)
# total = price*quantity
# print(f"Your price is : {total}")

# String Index
# my_name = "Saleh Sazzad"
# [start:stop:stepover]
# print(my_name[:5:1])
# print(my_name[6::1])
# print(my_name[4::-1])
# print(my_name[:5:-1])

# Password Checker
# username = input('What is your username?')
# password = input("Your password?")
# password_length = len(password)
# hidden_password = "#" * password_length
# print(f"Dear {username}, your password, {
#       hidden_password} is {password_length} chAracters long!")

# List Slicing
# amazon_cart = ['notebooks', 'sunglass', 'toys', 'grapes']
# amazon_cart[0] = 'laptop'
# daraz = amazon_cart[:]
# daraz[0] = 'Quantum Computer'
# print(f"Daraz store have: {daraz}")
# print(f"AMazon have:  {amazon_cart} \n")
# print("Copying with another method yield - ")
# amazon_cart2 = amazon_cart
# amazon_cart2[1] = 'Raybon'
# print(amazon_cart)
# print(amazon_cart2)
# print(" \nThat got pointer property - amazon_cart2 = amazon_cart //  ")
# print("That successfully assigns - daraz = amazon_cart[:] ")

# Creating Dictionary
# user1 = {                                      #One way
#     'name': "Saleh Sazzad",
#     'Date_of_birth': "18-01-2001",
#     'gender': 'male'
# }
# user2 = dict(name="Sajid Hasan")               #Second way
# print(user1)
# print(user2)

# Dictionary Update
# profile = {
#     'age': 18,
#     'username': "Sibgut",
#     'weapons': "Gun",
#     'is_active': True,
#     'clan': "Emirate"
# }
# print(profile.keys())
# profile['weapons'] = "Sword"
# profile.update({'is_banned': False})
# profile['is_banned'] = True
# profile2 = profile.copy()
# profile2.update({'age': 23, 'username': "Saleh"})
# print(profile2)
# print(profile)


school = {'Bobby', 'Tammy', 'Jammy', 'Sally', 'Danny'}
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']
s_days_a_list = set(attendance_list)  # Converting list into set
print(f"Students who missed the class: {school.difference(s_days_a_list)}")

# List can directly be used
print(f"Or this way: {school.difference(attendance_list)}")
