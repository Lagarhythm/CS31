# Christopher Earl, Chapter 6 Lab 2
import os


def main():

    # Part 1
    display_data()
    modify_num()

    # Part 2
    try:
        even = 0
        odd = 0
        with open('numbers.txt', 'r') as nums:
            for num in nums:
                if int(num) % 2 == 0:
                    even += 1
                else:
                    odd += 1
        print('The file contains', even, 'even numbers and', odd, 'odd numbers.')
    except IOError:
        print('File did not open.')
    except ValueError as err:
        print(err)


def display_data():
    with open('nba.txt', 'r') as nba:
        name = nba.readline()
        while name != '':
            name = name.rstrip('\n')
            num = nba.readline().rstrip('\n')
            team = nba.readline().rstrip('\n')
            print(name, 'wears number', num, 'for the', team)
            name = nba.readline()


def modify_num():
    found = False
    find_this = input('Enter the name you want to change data for: ')
    with (open('nba.txt', 'r') as nba,
          open('temp.txt', 'w') as temp):
        name = nba.readline().rstrip('\n')
        while name != '':
            num = nba.readline().rstrip('\n')
            team = nba.readline().rstrip('\n')
            if name == find_this:
                new_num = input('Enter new number: ')
                temp.write(name + '\n')
                temp.write(new_num + '\n')
                temp.write(team + '\n')
                found = True
            else:
                temp.write(name + '\n')
                temp.write(num + '\n')
                temp.write(team + '\n')
            name = nba.readline().rstrip('\n')
    # Both files now closed
    # Delete the original nba.txt
    os.remove('nba.txt')
    # Rename the temp file to nba.txt
    os.rename('temp.txt', 'nba.txt')
    if found:
        print('File has been updated.')
        display_data()
    else:
        print(find_this, ' was not found in the file.')


main()
