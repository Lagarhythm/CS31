# Christopher Earl, Ch5 Lab 1
# Part 1, 2 & 3

def main():
    team = int(input('Type 1 for Kings, 2 for Ducks, 3 for Knights, '
                     '4 for Sharks, anything else to quit '))
    while 1 <= team <= 4:
        match team:
            case 1:
                kings()
            case 2:
                ducks()
            case 3:
                knights()
            case _:
                sharks()
        input('Press Enter to continue')
        team = int(input('Type 1 for Kings, 2 for Ducks, 3 for Knights, '
                         '4 for Sharks, anything else to quit '))
    print("That's all!")


def kings():
    print('The Los Angeles Kings began NHL play in 1967.')
    print('their home arena is the Crypto.com Arena.')
    print()


def ducks():
    print('The Anaheim Ducks began NHL play in 1993.')
    print('their home arena is the Honda Center.')
    print()


def knights():
    print('The Vegas Golden Knights began NHL play in 2017.')
    print('their home arena is the T-Mobile Arena.')
    print()


def sharks():
    print('The San Jose Sharks began NHL play in 1991.')
    print('their home arena is the SAP Center.')
    print()


# Don't forget to call main
main()



