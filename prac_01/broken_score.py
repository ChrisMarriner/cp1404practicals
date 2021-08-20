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


score = float(input("Enter score: "))
if 50 > score >= 0:
    print("Bad")
elif 50 <= score < 90:
    print("Pass")
elif 90 <= score <= 100:
    print("Excellent")
else:
    print("Invalid score entered.")
