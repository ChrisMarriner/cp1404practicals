"""
Christopher Marriner
"""

# 1.
# OUTPUT_FILE = "name.txt"
# out_file = open(OUTPUT_FILE, "w")
# name = input("Name: ")
# print(name, file=out_file)
# out_file.close()
#
# # 2.
# INPUT_FILE = "name.txt"
# in_file = open("name.txt", "r")
# name = in_file.read().strip()
# print("Your name is", name)
# in_file.close()

# # 3.
# INPUT_FILE = "numbers.txt"
# in_file = open(INPUT_FILE, "r")
# number_1 = (int(in_file.readline()))
# number_2 = (int(in_file.readline()))
# print(number_1 + number_2)
# in_file.close()

# 4.
INPUT_FILE = "numbers.txt"
total = 0
in_file = open(INPUT_FILE, "r")
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()
