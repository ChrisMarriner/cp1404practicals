"""
Christopher Marriner

Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.


PSEUDOCODE:

get sales
while sales >= 0
    if sales are below 1000
        calculate bonus
        display bonus
    if sales are above 1000
        calculate bonus
        display bonus
    get sales

"""
BONUS_THRESHOLD = 1000
SALES_MINIMUM = 0.10
SALES_MAXIMUM = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < BONUS_THRESHOLD:
        sales = sales * SALES_MINIMUM
        print('Bonus: ${:.0f}'.format(sales))
    if sales >= BONUS_THRESHOLD:
        sales = sales * SALES_MAXIMUM
        print('Bonus: ${:.0f}'.format(sales))
    sales = float(input("Enter sales: $"))



