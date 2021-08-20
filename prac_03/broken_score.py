"""
Christopher Marriner

CP1404/CP5632 - Practical
Broken program to determine score status


PSEUDOCODE:

get score
if score is between 0 and 50
    display "bad"
else if score is between 50 and 90
    display "pass"
else if score is between 90 and 100
    display "Excellent"
else
    display "Invalid score"

"""

import random


def main():
    score = float(input('Enter score: '))
    print(get_status(score))
    score = random.randint(0, 101)
    print("Score: {} = ".format(score), get_status(score))


def get_status(score):
    if 50 > score >= 0:
        return "Bad"
    elif 50 <= score < 90:
        return "Pass"
    elif 90 <= score <= 100:
        return "Excellent"
    else:
        return "Invalid score entered."


main()
