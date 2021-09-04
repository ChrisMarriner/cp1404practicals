"""
Christopher Marriner
CP1404 Practical
Emails program

Pseudocode:
get email until blank input
check for name in email
ask if name in email
if name in email
    add to dictionary
if name not in email
    get name
    add to dictionary
print name and email from dictionary
"""


def main():
    name_email_dict = {}
    email = input("Email: ")
    while email != "":
        name = get_names_from_email(email)
        user_input = input("Is your name {}? (Y/n) ".format(name))
        if user_input.upper() != "Y" and user_input != "":
            name = input("Name: ")
        name_email_dict[email] = name
        email = input("Email: ")
    for email, name in name_email_dict.items():
        print("{} ({})".format(name, email))


def get_names_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
