"""
Christopher Marriner

CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
The ValueError will occur if the user enters a character instead of a number.

2. When will a ZeroDivisionError occur?
ZeroDivisionError will occur if the user enters 0 as the denominator

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
I added a "while denominator is equal to zero" loop
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")
