"""
Christopher Marriner
CP1404 - "Quick Pick" Lottery Ticket Generator

Pseudocode:
import random
get number of quick picks
error checking
in range of number of quick picks
    make empty list for quick picks
    in range of NUMBERS PER LINE
    generate random numbers
    add random numbers to quick picks list
    sort quick picks list
display quick picks

"""

import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("Number of quick picks: "))
    number_of_quick_picks = check_for_errors(number_of_quick_picks)
    calculate_quick_picks(number_of_quick_picks)


def calculate_quick_picks(number_of_quick_picks):
    for i in range(number_of_quick_picks):
        quick_picks = []
        for x in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_picks:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join("{:2}".format(number) for number in quick_picks))


def check_for_errors(number_of_quick_picks):
    while number_of_quick_picks <= 0:
        print("Number of quick picks cannot be 0 or less.")
        number_of_quick_picks = int(input("Number of quick picks: "))
    return number_of_quick_picks


main()
