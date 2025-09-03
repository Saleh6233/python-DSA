# import utility
# import shopping.shopping_cart
# from utility import multiply, divide
# from shopping.more_shopping.shopping_cart import buy


# class Student():
#     pass


# if __name__ == '__main__':

#     print(multiply(2, 3))
#     print(buy("Laptop"))
#     st1 = Student()
#     print(type(st1))


# import random
# from random import seed, shuffle

# seed(1)

# my_list = [1, 2, 3, 4, 5]

# shuffle(my_list)

# print(my_list)

import sys
from random import randint, seed

seed(1)
answer = randint(1, 10)


while True:
    try:
        guess = int(input('Guess a number 1~10 \n'))
        if guess > 0 and guess < 11:

            if guess == answer:
                print("You Guessed right!")
                break
            elif (guess > answer):
                print("You guessed it bigger!")

            else:
                print("You guessed it smaller!")

        else:
            print("Number is out of range! ", end="")

    except ValueError:
        print("Please enter a valid number! ", end="")

        continue
