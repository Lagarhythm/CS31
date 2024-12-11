def main():
    cartoons = [ ['','',''], ['','',''], ['','',''], ['','',''],
                 ['','',''], ['','',''], ['','',''], ['','',''] ]
    rows = 8
    cols = 3
    # FYI: The cartoons list has 8 rows and 3 columns
    #
    # Using a with statement, open the cartoons.txt file for reading
    # and use inputfile for the file object name.
    #
    # Within the with statement, call the readData function with
    # the needed parameters.
    #
    # After the with statement, call the display function with
    # the needed parameters.
    #
    # Add a line of output that displays your first and last name.
    # Example: Submitted by Kyle Muldrow (use YOUR first and last name)

    with open('cartoons.txt', 'r') as inputfile:
        readData(cartoons, inputfile, rows, cols)

    display(cartoons, rows)

    print('Submitted by Christopher Earl')

def readData(the_list,infile,rows_in_list,cols_in_list):
    # This function has four parameters: a two-dimensional list, a file object,
    # the number of rows in the list, and the number of columns in the list.
    #
    # Use nested while loops to read data for each character from the file
    # and store each character's data in each row of the list.
    # The while loops must use a test condition containing an actual boolean
    # expression with a comparison operator and not contain any break or
    # continue statements.
    #
    # The columns on each row must contain the following data, in this order:
    # - The character's name
    # - The year the character debuted
    # - The studio that produces the character
    # Use the rstrip function to remove '\n' from each item read from the file.
    col_counter = 0
    row_counter = 0
    while row_counter != rows_in_list:
        col_counter = 0
        while col_counter != cols_in_list:
            data = infile.readline().rstrip()
            the_list[row_counter][col_counter] = data
            col_counter += 1
        row_counter += 1

def display(the_list,rows_in_list):
    # This function has two paramters: a two-dimensional list and
    # the number of rows in the list.
    #
    # Use a for loop with the range function to put the data in each row of the file
    # into a sentence and display the sentence. There must be no gaps between lines of output.

    for data in the_list:
        print(f'{data[0]} debuted in {data[1]} in a a cartoon prduced by {data[2]}')
main()