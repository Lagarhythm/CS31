####################################################
# CS 31, Prof. Muldrow
# Name: Christopher Earl
# Assignment: Chapter 3, Homework
# Due Date: 9/15/24
####################################################

def star_underline(program_name):
    print()
    print(program_name)
    for char in program_name:
        print("*", end="")
    print("\n")

# Assignment 1

programOne = "Color Mixer"
star_underline(programOne)

firstColor = input("Enter a primary color: ")

secondColor = input("Enter a second primary color: ")

match (firstColor, secondColor):
    case ("red", "red") | ("blue", "blue") | ("yellow" | "yellow"):
        print("Your color is", firstColor)
    case ("red", "blue") | ("blue", "red"):
        print(firstColor, "mixed with", secondColor, "makes purple")
    case ("red", "yellow") | ("yellow", "red"):
        print(firstColor, "mixed with", secondColor, "makes orange")
    case ("blue", "yellow") | ("yellow", "blue"):
        print(firstColor, "mixed with", secondColor, "makes green")
    case _:
        print("Invalid color combination")

# Assignment 2

programTwo = "Roulette Pocket Color"
star_underline(programTwo)

userNum = int(input("Enter a number between 0 and 36: "))

match userNum:
    case userNum if userNum < 0 or userNum > 36:
        print("Invalid number")
    case 0:
        print("Your pocket is green")
    case userNum if 1 <= userNum <= 10:
        pocketColor = userNum % 2
        if pocketColor == 1:
            # print("WHY ARE YOU PRINTING HERE?") #debug
            print("Your pocket color is red")
        else:
            print("Your pocket color is black")
    case userNum if 11 <= userNum <= 18:
        pocketColor = userNum % 2
        if pocketColor == 1:
            print("Your pocket color is black")
        else:
            print("Your pocket color is red")
    case userNum if 19 <= userNum <= 28:
        pocketColor = userNum % 2
        if pocketColor == 1:
            print("Your pocket color is red")
        else:
            print("Your pocket color is black")
    case userNum if 29 <= userNum <= 36:
        pocketColor = userNum % 2
        if pocketColor == 1:
            print("Your pocket color is black")
        else:
            print("Your pocket color is red")
    case _:
        print("Invalid number")

# def even_odd(number):
#     modified_number = number % 2
#     return modified_number

programThree = "Software Discount"
star_underline(programThree)

softwareCost = 99
softwareQuantity = int(input("How many software package would you like to purchase? "))

match softwareQuantity:
    case softwareQuantity if 1 <= softwareQuantity <= 10:
        totalPrice = softwareQuantity * softwareCost
        finalPrice = totalPrice
    case softwareQuantity if softwareQuantity <= 19:
        totalPrice = softwareQuantity * softwareCost
        discount = totalPrice * .1
        finalPrice = totalPrice - discount
    case softwareQuantity if softwareQuantity <= 49:
        totalPrice = softwareQuantity * softwareCost
        discount = totalPrice * .2
        finalPrice = totalPrice - discount
    case softwareQuantity if softwareQuantity <= 99:
        totalPrice = softwareQuantity * softwareCost
        discount = totalPrice * .3
        finalPrice = totalPrice - discount
    case softwareQuantity if softwareQuantity >= 100:
        totalPrice = softwareQuantity * softwareCost
        discount = totalPrice * .4
        finalPrice = totalPrice - discount
    case _:
        print("Invalid number")


print(f"Your total price is ${finalPrice:.2f}")


# Assignment 4 (Did this one by accident; read 13 instead of 12 on the assignments)

programFour = "Shipping Cost"
star_underline(programFour)

packageWeight = float(input("Enter package weight: "))

match packageWeight:
    case packageWeight if 0 <= packageWeight <= 2.00:
        packagePrice = packageWeight * 1.50
        print(f"Shipping charge ${packagePrice:.2f}")
    case packageWeight if packageWeight <= 6:
        packagePrice = packageWeight * 3.00
        print(f"Shipping charge ${packagePrice:.2f}")
    case packageWeight if packageWeight <= 10:
        packagePrice = packageWeight * 4.00
        print(f"Shipping charge ${packagePrice:.2f}")
    case packageWeight if packageWeight > 10:
        packagePrice = packageWeight * 4.75
        print(f"Shipping charge ${packagePrice:.2f}")