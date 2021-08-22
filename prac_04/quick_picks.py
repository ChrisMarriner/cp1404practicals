"""
Christopher Marriner
CP1404 - "Quick Pick" Lottery Ticket Generator

Pseudocode:
import random
get number of quick picks
error checking
make empty list for quick picks

display quick picks

"""

import random


def main():
    number_of_quick_picks = int(input("Number of quick picks: "))
    error_checking(number_of_quick_picks)


def error_checking(number_of_quick_picks):
    while number_of_quick_picks < 0:
        print("Number of quick picks cannot be 0 or less.")
        number_of_quick_picks = int(input("Number of quick picks: "))


main()
