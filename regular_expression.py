import re

"""  Email Validation via regex  """

pattern = re.compile(r"(^[a-zA-z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-z0-9-]+$)")

# email = input("Please enter  an email\n")

# a = pattern.search(email)

while True:
    email = input("Please enter  an email: \n")
    a = pattern.search(email)
    if (a is None):
        print("Email is invalid.", end=" ")
    else:
        print("Thank you for your cooperation.")
        break
