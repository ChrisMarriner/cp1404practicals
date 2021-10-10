"""
Christopher Marriner
unreliable car test program
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Testing different cars on reliability multiple times"""
    car_1 = UnreliableCar("New Car", 100, 90)
    car_2 = UnreliableCar("Old Car", 100, 9)
    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(car_1.name, car_1.drive(i)))
        print("{:12} drove {:2}km".format(car_2.name, car_2.drive(i)))
    print(car_1)
    print(car_2)


main()
