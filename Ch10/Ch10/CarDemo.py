import Car


def main():
    my_car = Car.Car('2016', 'Subaru', 'Outback')
    print(my_car)
    for x in range(5):
        my_car.speed_up()
        print(my_car)
    print()
    for x in range(5):
        my_car.slow_down()
        print(my_car)


main()
