import os

# To make data folder in current directory
# os.mkdir("data")

# if (not os.path.exists("data")):  # os.path.exists checks  if such folder exists
#     os.mkdir("data")
#     print("data folder has been created!\n", )
# else:
#     print("data folder already exists!\n")

# for i in range(0, 100):
#     # In data folder we are creating Day1, Day2 ..... Day100 folders
#     os.mkdir(f"data/Day{i+1}")

# for i in range(0, 100):
#     # In data folder we are renaming Day1, Day2 ..... Day100 folders with Day 1, Day 2 ..... Day 100
#     os.rename(f"data/Data {i+1}", f"data/Day {i+1}")

# print('\n')
# folders = os.listdir("data")

# print(type(folders[9]))

data_path = r"C:\Users\DELL\Documents\All ML Practise\cse445 project ver 2\dataset"


labels = os.listdir(data_path)
# print(labels)

for speaker in labels:
    speaker_path = os.path.join(data_path, speaker)
    if os.path.isdir(speaker_path):
        print(f"Yes it is {speaker}")

        file_path = os.listdir(speaker_path)

        print(file_path, "\n")

    # print(speaker_path, "\n")

    # print(os.getcwd())
