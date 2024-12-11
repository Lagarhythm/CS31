def main():
    num1 = float(input('Input first number: '))
    num2 = float(input('Input second number: '))
    doMath(num1, num2)
    # Add a line of code to main that prints a sentence with your first and last name.
    # Example: Submitted by Kyle Muldrow (use YOUR first and last name)
    # Do not make any other changes to main.
    print("Submitted by Christopher Earl")
def doMath(n1, n2):
    # Add code to this function using an if-elif-else statement to do the following:
    # - If the first parameter is greater than 10 and the second parameter is less than five,
    #   add 3 times the first parameter to 2 times the second parameter and display the result
    #   rounded to three decimal places in a sentence. (Example: The sum is 15)
    if n1 > 10 and n2 < 5:
        n3 = (n1 * 3) + (n2 * 2)
        print(f'The sum is {n3:.3f}')
    #
    # - If the first parameter is greater than or equal to 15 and the second parameter is greater than 7,
    #   divide the first parameter by 3, raise the second parameter to the second power, add these values,
    #   and display the result rounded to two decimal places in a sentence.
    elif n1 >= 15 and n2 > 7:
        n3 = (n1 / 3) + n2**2
        print(f'The sum is {n3:.2f}')
    #
    # - If the first parameter is less than 4 and the second parameter is greater than or equal to 10,
    #   raise the first parameter to the third power, divide the second parameter by 5, add these values,
    #   and display the result rounded to four decimal places in a sentence.
    elif n1 < 4 and n2 >= 10:
        n3 =n1**3 + (n2 - 5)
        print(f'The sum is {n3:.4f}')
    #
    # - Otherwise, add the two parameters and display the sum to one decimal place in a sentence.
    else:
        n3 = n1 + n2
        print(f'The sum is {n3:.1f}')
    #
    # - You must use an f-string to do all rounding.

main()