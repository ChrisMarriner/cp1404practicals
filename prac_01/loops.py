"""
Christopher Marriner
CP1404 - Practical
"""

# 1
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# 2
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# 3
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# 4
stars = int(input("Number of stars: "))
for i in range(stars):
    print("*", end='')
print()

# 5
for i in range(1, stars + 1):
    print('*' * i)
print()
