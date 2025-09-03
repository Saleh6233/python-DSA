# Lesson 1
# myMarks=80
# curve=0.1
# total=myMarks+(myMarks*curve)
# print("My total mark is " , total  )

# Lesson 2
# string1="Assalamu Alaikum"
# print(string1.upper())
# string2="Saleh, have you done the home work?"
# print(string2.split())
# print(string2.split(","))
# print("The first string is: " ,string2[0], "; The last string is: " , string2[-1])
# print("Second word of string is: ", string2[7:11])

# first_name="Saleh"
# last_name="Sazzad"
# print(f"Ahlan Wa Sahlan '{first_name} {last_name}'")

# # Lesson 3
# myvar="NEW"
# mylist=[100,200,300,400,500]
# mylist.append(myvar)
# mylist.insert(0,myvar)
# print(f"My list is: {mylist}. Removing last item- " )
# mylist.pop(6)
# print(f"My new list: {mylist}. Let's reverse it- ")
# mylist.reverse()
# print(f"My new list: {mylist}.")

# # Lesson 4
# employees = {"chief":"Rianur", "ceo":"Mustafizur"}
# # Add new value
# employees["waiter"]= "Irfan"
# print(employees)
# print(f"I repeat our waiter is: {employees['waiter']}")
# print("Let's kick our chief")
# # update
# employees["chief"]= "Saleh"
# print(f"The new chief is {employees['chief']}")
# print(employees.keys())
# print(employees.values())
# print(employees.items())

# # Lesson 5
# mytuple=(1,2,3,4)
# print(mytuple)

# password= "mypass123"
# database_pass= "mypass1234"
# admin= True
# if password==database_pass:
#   print("Ahlan wa Sahlan")
# elif admin:
#   print("Ahlan wa Sahlan Admin saheb")
# else:
#   print("Ma'As Salam")

# Lesson 5
# sales= [1,2,3,4,5]
# for num in sales:
#   print(f"Example sale of: {num}")

# employees = {"chief":"Rianur", "ceo":"Mustafizur"}
# for position in employees:
#   print(f"The {position} is held by {employees[position]}")

# mylist = [('a','b'),('c','d'),(1,2)]
# for item in mylist :
#   print(item)
# for item1,item2 in mylist:
#   print(f"{item1} -> {item2}")

# n=1
# while n<=5:
#   print(f"N is currently: {n} ")
#   n=n+1

# Lesson 6

# def checker(list_to_check):
#     for num in list_to_check:
#         if num == 11:
#             return True

#     return False


# numbList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13]
# print(checker(numbList))

# input('what is your name?')

a, b = 3, 2

sum = a+b

sub = a-b

mul = a*b

print(sum, "\n", sub, "\n", mul)
