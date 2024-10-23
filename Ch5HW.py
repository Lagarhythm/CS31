####################################################
# CS 31, Prof. Muldrow
# Name: Christopher Earl
# Assignment: Chapter 3, Homework
# Due Date: 10/13/24
####################################################
import random


def main():

    count_even_odd(100)
    print()

    print('List of prime numbers between 1 & 100')
    for i in range(1, 101):
        if is_prime(i):  # PyCharm showed me how to shorten this expression from - if is_prime(i) == True:
            print(i)
    print()

    print('Future Value')
    principle = float(input("Enter the account's present value : "))
    interest = float(input('Enter the monthly interest rate: '))
    months = float(input('Enter the number of months the money will be left in the account: '))
    print(f'The future value of your account is ${future_value(principle, interest, months):.2f}')


def count_even_odd(num):
    even = 0
    odd = 0
    for i in range(0, num):
        rand_num = random.randint(1, 1000)
        # print(rand_num)
        remainder = mod_number(rand_num, 2)
        if remainder == 0:
            even += 1
        else:
            odd += 1
    print(f'From the random numbers generated there are {even} that are even & {odd} that are odd')


def mod_number(num, div):
    divided_num = num % div
    return divided_num


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        remainder = mod_number(num, i)
        if remainder == 0:
            return False
    return True


def future_value(principle, interest, months):
    interest = interest / 100
    value = principle * (1 + interest)**months
    return value


main()

