"""
Christopher Marriner - CP1404

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
# 1.
NUMBER_OF_QUESTIONS = 5


def main():
    numbers = []
    for i in range(NUMBER_OF_QUESTIONS):
        number = int(input("Number: "))
        numbers.append(number)
    print("The first number is: ", numbers[0])
    print("the last number is: ", numbers[-1])
    print("The smallest number is: ", min(numbers))
    print("The largest number is: ", max(numbers))
    print("The average of the numbers is: ", sum(numbers) / len(numbers))


main()
