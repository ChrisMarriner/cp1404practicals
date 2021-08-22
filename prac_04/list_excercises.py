"""
Christopher Marriner - CP1404

# 1. Basic List Operations

Pseudocode:
numbers as a empty list
ask for number NUMBER_OF_QUESTION times
add number to numbers list
display the first number
display the last number
display the smallest number
display the largest number
calculate the average of numbers
display the average of numbers

"""

NUMBER_OF_QUESTIONS = 5


def main():
    numbers = []
    for i in range(NUMBER_OF_QUESTIONS):
        number = int(input("Number: "))
        numbers.append(number)
    display_numbers(numbers)


def display_numbers(numbers):
    print("The first number is: ", numbers[0])
    print("the last number is: ", numbers[-1])
    print("The smallest number is: ", min(numbers))
    print("The largest number is: ", max(numbers))
    print("The average of the numbers is: ", sum(numbers) / len(numbers))


main()

"""
# 2. Woefully inadequate security checker

Pseudocode:
list of usernames
get username
if username is in list
    display Access Granted
else
    display Access Denied
"""


def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Username: ")
    display_access_permission(username, usernames)


def display_access_permission(username, usernames):
    if username in usernames:
        print("Access Granted!")
    else:
        print("Access Denied!")


main()
