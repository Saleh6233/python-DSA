# my_file = open('test.txt')

# print(my_file.read())

# my_file.seek(0)
# print(my_file.readline())

# my_file.seek(0)
# print(my_file.readlines())

# print("Reading Completed!")

# my_file.close()


##### Standard a way to read file#########

# with open('test.txt') as my_file:
#     print(my_file.readlines())

# print("Reading Completed!")

# with open('test.txt', mode='a') as my_file:
#     text = my_file.write("\nI am doing fine")
#     print(text)

# print("Reading Completed!")

from pathlib import Path
with open('conf.txt', mode='w') as my_file:
    text = my_file.write("Alhamdulillah")
    print(text)

print("Reading Completed!")
