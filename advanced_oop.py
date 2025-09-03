# # Given the below class:
# class Cat:
#     species = 'mammal'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # 1 Instantiate the Cat object with 3 cats
# ahmed = Cat("ahmed", 3)
# sakina = Cat("sakina", 2)
# bush = Cat("bush", 5)

# # 2 Create a function that finds the oldest cat


# def oldest_cat(*age):
#     oldest_age = 0
#     for item in age:
#         if oldest_age < item:
#             oldest_age = item
#     return oldest_age


# # 3 Print out: "The oldest cat is x years old.".
# # x will be the oldest cat age by using the function in #2


# print(f"\nThe oldest cat is {oldest_cat(
#     ahmed.age, sakina.age, bush.age)} years old")


# class Pets():
#     animals = []

#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())


# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'


# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# # 1 Add nother Cat


# class Bua(Cat):
#     def steal(self, things):
#         return f'{things} have stolen it!!'


# # 2 Create a list of all of the pets (create 3 cat instances from the above)
# cat1 = Simon("simon", 4)
# cat2 = Sally("sally", 3)
# cat3 = Bua("phazil_bua", 7)

# my_cats = [cat1, cat2, cat3]

# # 3 Instantiate the Pet class with all your cats use variable my_pets
# # class Pets():
# #     animals = []

# #     def __init__(self, animals):
# #         self.animals = animals

# #     def walk(self):
# #         for animal in self.animals:
# #             print(animal.walk())

# my_pets = Pets(my_cats)


# # 4 Output all of the cats walking using the my_pets instance

# my_pets.walk()

# # for each_cat in my_pets.animals:
# #     each_cat.

# from functools import reduce

# # 1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']


# def capitalize(string):
#     return string.upper()


# print(list(map(capitalize, my_pets)))


# # 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5, 4, 3, 2, 1]

# print(list(zip(my_strings, sorted(my_numbers))))


# # 3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]


# def is_smart_student(score):
#     return score > 50


# print(list(filter(is_smart_student, scores)))


# # 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
# def accumulator(acc, item):
#     return acc + item


# print(reduce(accumulator, (my_numbers + scores)))


# my_list = [5, 4, 3]
# print(list(map(lambda item: item*item, my_list)))


# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = {
#     "name": "Sorna",
#     # changing this will either run or not run the message_friends function.
#     "valid": True,
# }


# def authenticated(fn):
#     # code here
#     def wrapper(*args, **kwargs):
#         if args[0]["valid"]:
#             return fn(*args, **kwargs)
#         else:
#             return print("invalid user")

#     return wrapper


# @authenticated
# def message_friends(user):
#     print("message has been sent")


# message_friends(user1)
