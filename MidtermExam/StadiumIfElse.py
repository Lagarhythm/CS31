def main():
    for x in range(11):
        ch = str(input('Enter B, D, E, P or R: '))
        print(stadium(ch))
    # When the for loop is finished, add a line of code to main that prints a sentence with your first and last name.
    # Example: Submitted by Kyle Muldrow (use YOUR first and last name)
    # Do not make any other changes to main.
    print("Submitted by Christopher Earl")
def stadium(ch):
    # Write code for this function using an if-elif-else statement do to the following:
    # - If the parameter is 'b' or 'B', return the string 'Banc of California Stadium is home to Los Angeles FC'
    if ch == "b" or ch == "B":
        return str("Banc of California Stadium is home to Los Angeles FC")
    # - If the parameter is 'd' or 'D', return the string 'Dignity Health Sport Park is home to the LA Galaxy'
    elif ch == "d" or ch == "D":
        return str("Dignity Health Sport Park is home to the LA Galaxy")
    # - If the parameter is 'e' or 'E', return the string 'Earthquakes Stadium is home to the San Jose Earthquakes'
    elif ch == "e" or ch == "E":
        return str("Earthquakes Stadium is home to the San Jose Earthquakes")
    # - If the parameter is 'p' or 'P', return the string 'Providence Park is home to the Portland Timbers'
    elif ch == "e" or ch == "P":
        return str("Providence Park is home to the Portland Timbers")
    # - If the parameter is 'r' or 'R', return the string 'Rio Tinto Stadium is home to Real Salt Lake'
    elif ch == "r" or ch == "R":
        return str("Rio Tinto Stadium is home to Real Salt Lake")
    # - If the parameter is anything else, return the string 'Invalid Character entered'
    else:
        return str("Invalid Character entered")

main()