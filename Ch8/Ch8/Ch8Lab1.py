# Christopher Earl, Chapter 8 Lab 1

def main():
    # Part 1
    again = 'y'
    while again == 'y' or again == 'Y':
        num = input('Enter a sequence of numbers (no spaces): ')
        print('Sum of digits in', num, ' = ', get_sum(num))
        again = input('Again? (y/n) ')

    # Part 2
    again = 'y'
    while again == 'y' or again == 'Y':
        title = input('Enter a one-word movie title: ')
        if len(title) <= 4:
            code = title
        elif len(title) == 5:
            code = title[::2]
        else:
            code = title[:5:2] + title[-1]
        year = input('Enter the four-digit year movie was released: ')
        code += year[2:]
        print('Code for', title, 'is', code)
        again = input('Again? (y/n) ')

def get_sum(num):
    sum = 0
    for ch in num:
        sum += int(ch)
    return sum


main()