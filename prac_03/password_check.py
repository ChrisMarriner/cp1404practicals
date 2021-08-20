"""
Christopher Marriner
CP1404 - Password Checker
"""

MINIMUM_LENGTH = 4


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print('*' * len(password))


def get_password():
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        password = input("Password needs to be at least {} characters: ".format(MINIMUM_LENGTH))
    return password


main()
