"""
Christopher Marriner

CP1404 - Practical

PSEUDOCODE:

get number of items
while number of items is less than or equal to 0
    display error message
    get number of items
get price of items in range of number of items
    calculate total price of items
if total price of items is greater than 100
    calculate total price with discount
display total price

"""

DISCOUNT = 0.9
total_price = 0

number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price = total_price + price_of_item
if total_price > 100:
    total_price = total_price * DISCOUNT
print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))
