"""
Christopher Marriner
Taxi simulator program
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    """Shows list of taxis available"""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def main():
    """Gets menu choice from user and shows final bill on quit"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    current_taxi = None
    print("Let's drive!")
    print("(q)uit, (c)hoose taxi, (d)rive")
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            current_taxi = choose_taxi(current_taxi, taxis)
        elif menu_choice == "d":
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_bill))
        print("(q)uit, (c)hoose taxi, (d)rive")
        menu_choice = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def drive_taxi(current_taxi, total_bill):
    if current_taxi:
        current_taxi.start_fare()
        distance_to_drive = float(input("Drive how far? "))
        current_taxi.drive(distance_to_drive)
        trip_cost = current_taxi.get_fare()
        print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
        total_bill += trip_cost
    else:
        print("You need to choose a taxi before you can drive")
    return total_bill


def choose_taxi(current_taxi, taxis):
    print("Taxis available: ")
    display_taxis(taxis)
    taxi_choice = int(input("Choose taxi: "))
    try:
        current_taxi = taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")
    return current_taxi


main()
