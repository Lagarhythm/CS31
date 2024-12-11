import random

def main():
   howmany = int(input('How many numbers? '))
   big, small = bigsmall(howmany)
   print('Of the numbers generated,',big,'were greater than 50 and',small,'were 50 or less')
   # Add a line of code to main that prints a sentence with your first and last name.
   # Example: Submitted by Kyle Muldrow (use YOUR first and last name)
   # Do not make any other changes to main.
   print("Submitted by Christopher Earl")

def bigsmall(num):
    # Write code for this function as follows:
    # - Use a while loop to determine if the parameter is greater than 1.
    # - As long as it is not greater than 1, do the following:
    #   - Display a message to the user saying the value must be greater than 1
    #     and to try again.
    #   - Prompt the user to enter how many character there will be.
    while num <= 1:
       print("Must be greater than 1. Try again.")
       num = int(input('How many numbers? '))
    #
    # - The while loop must use an actual boolean expression with a comparison
    # - operator (<, >, <=, >=, ==, or !=). No break or continue statements allowed.
    #
    # - After the while loop is finished, use a for loop with the range function
    #   to generate each character in this way:
    #   - Generate a random integer between 1 and 200.
    #   - Display the number, using the loop counter variable to say which one it is.
    #     Example: Number 1 = 100, Number 2 = 50, and so on.
    #   - If the number is greater than 50, add 1 to a counter for numbers greater than 50;
    #     otherwise, add 1 to a counter for numbers 50 or less.
    greaterThan = 0
    lessThan = 0
    for i in range(1, num + 1):
         randNum = random.randint(1, 200)
         if randNum > 50:
            greaterThan += 1
         else:
            lessThan += 1
         print("number",i,"=",randNum)
    return greaterThan, lessThan
    #
    # - When the for loop ends, return both counters.

main()
