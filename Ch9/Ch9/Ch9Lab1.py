# Christopher Earl, Chapter 9 Lab 1

def main():
    # Part 1
    schools1 = {
        'USC': 'Los Angeles',
        'Oregon': 'Eugene',
        'Arizona': 'Tucson',
        'Utah': 'Salt Lake City'
    }

    schools2 = {
        'USC': 'Trojans',
        'Oregon': 'Ducks',
        'Arizona': 'Wildcats',
        'Utah': 'Utes'
    }

    again = 'y'
    while again == 'y' or again == 'Y':
        univ = input('Enter name of Western University: ')
        if univ in schools1:
            print(univ, 'is in', schools1[univ], 'and the sports team are the', schools2[univ])
        else:
            print(univ, 'is in invalid')
        again = input('Again (y/n) ')
    # Part 2
    medals = {}

    with open('medals.txt', 'r') as m:
        key = m.readline()
        while key != '':
            key = key.rstrip()
            gold = int(m.readline().rstrip())
            silver = int(m.readline().rstrip())
            bronze = int(m.readline().rstrip())
            medals[key] = [gold, silver, bronze]    # Each keu is associated with a list
            key = m.readline()

    # Part 3
    with open('medals2.txt', 'r') as m:
        key = m.readline()
        while key != '':
            key = key.rstrip()
            data = m.readline().rstrip()
            medals[key] = data.split()
            key = m.readline()

    display_data(medals)
    print()
    print('Keys: ', end='')
    for key in medals.keys():
        print(key, end=' ')
        for v in medals.values():
            print(v, end=' ')
    print()
    swede = medals.pop('Sweden')
    print('After pop: ')
    display_data(medals)


def display_data(d):
    for key in d:
        print(key, 'won', d[key][0], 'gold medals,', d[key][1], 'silver medals, and', d[key][2], 'bronze medals')


main()