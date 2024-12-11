class Car:
    def __init__(self, yr, mk, mod):
        self.__year = yr
        self.__make = mk
        self.__model = mod
        self.__speed = 0

    def speed_up(self):
        self.__speed += 10

    def slow_down(self):
        self.__speed -= 10

    def __str__(self):
        return self.__year + ' ' + self.__make + ' ' + self.__model + ' ' + 'Speed: ' + str(self.__speed) + ' MPH'