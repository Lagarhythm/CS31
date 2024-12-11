# Christopher Earl, Chapter 10 Lab 2
class Stadium:
    def __init__(self, n, cap, c):
        self.__name = n
        self.__capacity = cap
        self.__city = c
    def getName(self):
        return self.__name
    def getCapacity(self):
        return self.__capacity
    def getCity(self):
        return self.__city
    def __str__(self):
        return f'{self.__name} is in {self.__city} and has a capacity of {self.__capacity:,d}'
def main():
    s =[]
    with open('stadiums.txt', 'r') as stadiums:
        name = stadiums.readline()
        while name != '':
            name = name.rstrip('\n')
            capacity = int(stadiums.readline().rstrip('\n'))
            city = stadiums.readline().rstrip('\n')
            s.append(Stadium(name, capacity, city))
            name = stadiums.readline()
    for inst in s:
        print(inst)
    print()
    bigger(s[0], s[1])      # send first and second object to bigger()
    bigger(s[1], s[2])
def bigger(s1, s2):
    if s1.getCapacity() > s2.getCapacity():
        print(s1.getName(), 'in', s1.getCity(), 'is bigger than', s2.getName(), 'in', s2.getCity())
    else:
        print(s2.getName(), 'in', s2.getCity(), 'is bigger than', s1.getName(), 'in', s1.getCity())
main()