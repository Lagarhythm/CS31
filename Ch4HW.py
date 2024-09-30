####################################################
# CS 31, Prof. Muldrow
# Name: Christopher Earl
# Assignment: Chapter 4, Homework
# Due Date: 9/29/24
####################################################


def main():

# 12
    print()
    num = int(input("Enter a non-negative integer: "))
    x = num
    y = num
    z = num

    if num > 0:
        while 1 < z:
            y -= 1
            x *= y
            z -= 1
        print(f'{num:,}!={x:,}')
    elif num == 0:
        print("0!=1")
    else:
        print("Invalid factorial")

    print()

# 13

    pop = int(input("Enter the starting number of organisms: "))
    avg = int(input("Enter the average daily increase : "))
    days = int(input("Enter number of days to multiply: "))

    title1 = "Day Approximate"
    title2 = "Population"

    print()
    print(f'{title1:<20}',end='')
    print(title2)

    avg *= 0.01
    num_of_org = pop
    counter = 1

    while counter <= days:
        print(f'{counter:<20}',end='')
        print(f'{pop}')
        counter += 1
        num_of_org *= avg
        pop += num_of_org
        num_of_org = pop

    print()

# 15

    base_num = 6

    for row in range(0, base_num, +1):
        print("#",end='')
        for col in range(row):
            print(" ",end='')
        print("#")

main()