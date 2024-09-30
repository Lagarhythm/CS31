####################################################
# CS 31, Prof. Muldrow
# Name: Christopher Earl
# Assignment: Project 1
# Due Date: 10/02/24
####################################################
print()
print("10101010101010101010101010101010101010101010101010")
print("           Binary Burgers Order Program           ")
print("10101010101010101010101010101010101010101010101010")
print("")

print("Sandwich_Menu:")
print(f"\t{"1 == Hamburger":.<40}",end='')
print("$2.75")
print(f"\t{"2 == Cheeseburger":.<40}",end='')
print("$3.25")
print(f"\t{"3 == Chicken_Sandwich":.<40}",end='')
print("$2.50")
print(f"\t{"4 != sandwich #(null_sandwich)":<40}")
sandwich = int(input("Enter number: "))

match sandwich:
    case 1:
        sandwich = "Hamburger"
        sandwich_price = 2.75
    case 2:
        sandwich = "Cheeseburger"
        sandwich_price = 3.25
    case 3:
        sandwich = "Chicken_Sandwich"
        sandwich_price = 2.50
    case _:
        sandwich = ""
        sandwich_price = 0
print()

print("Side_Menu:")
print(f"\t{"1 == French_Fries":.<40}",end='')
print("$2.25")
print(f"\t{"2 == Onion_Rings":.<40}",end='')
print("$1.75")
print(f"\t{"3 == Side_Salad":.<40}",end='')
print("$1.50")
print(f"\t{"4 != side #(null_side)":<40}")
side = int(input("Enter number: "))

match side:
    case 1:
        side = "French_Fries"
        side_price = 2.25
    case 2:
        side = "Onion_Rings"
        side_price = 1.75
    case 3:
        side = "Side_Salad"
        side_price = 1.50
    case _:
        side = ""
        side_price = 0
print()

print("Drink_Menu:")
print(f"\t{"1 == Coca_Cola":<30}",end='')
print("3 == Lemonade")
print(f"\t{"2 == Sprite":<30}",end='')
print("4 == Water")
drink = int(input("Enter number: "))

match drink:
    case 1:
        drink_name = "Coke"
    case 2:
        drink_name = "Sprite"
    case 3:
        drink_name = "Lemonade"
    case _:
        drink_name = "Water"
print()

if 1 <= drink <= 3:
    print("Size:")
    print(f"\t{"1 == Small":.<40}", end='')
    print("$1.50")
    print(f"\t{"2 == Medium":.<40}", end='')
    print("$2.25")
    print(f"\t{"3 == Large":.<40}", end='')
    print("$2.75")
    drink_size = int(input("Enter number: "))
    match drink_size:
        case 1:
            drink_size = "Small_"
            drink_price = 1.50
        case 2:
            drink_size = "Medium_"
            drink_price = 2.25
        case 3:
            drink_size = "Large_"
            drink_price = 2.75
        case _:
            drink_size = "Medium_"
            drink_price = 2.25
else:
    drink_size = ""
    drink_price = 0
print()

subtotal = sandwich_price + side_price + drink_price
tax = subtotal * .08
total = subtotal + tax

print("Here is your order:")
if sandwich != "":
    print(f"{sandwich:<30}", end='')
    print(f"${sandwich_price:.2f}")
if side != "":
    print(f"{side:<30}", end='')
    print(f"${side_price:.2f}")
print(f"{drink_size + drink_name:<30}", end='')
print(f"${drink_price:.2f}")
print("-----------------------------------")
print(f"{"Subtotal":<30}${subtotal:.2f}")
print(f"{"Tax":<30}${tax:.2f}")
print(f"{"Total":<30}${total:.2f}")
print(f"{"(Cache Only)":>22}")