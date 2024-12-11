def main():
    # Use a with statement to open the kings.txt file for reading,
    # using inputfile as the file object name.
    # In the same with statement, open a file named stats.txt for writing,
    # using outputfile as the file object name.
    #
    # Within this first with statement, call the getData function
    # with the needed parameters.
    #
    # After the first with statement, use another with statement to open the
    # stats.txt file for reading, using showfile as the file object name.
    #
    # Within this with statement, call the display function with the
    # needed parameters.
    #
    # After the second with statement, add a line of output that displays
    # your first and last name
    # Example: Submitted by Kyle Muldrow (use YOUR first and last name)

    with open('kings.txt', 'r') as inputfile, open('stats.txt', 'w') as outputfile:
        getData(inputfile, outputfile)

    with open('stats.txt', 'r') as showfile:
        display(showfile)

    print('Submitted by Christopher Earl')

def getData(infile, outfile):
    # This function has two parameters, one for the input file and one for the output file.
    #
    # It must use a for loop to read each line of data from the file,
    # separate the data on that line by using the split() function,
    # add the goals and assists to get the total points (must use casting),
    # put all the data in a sentence (see output),
    # and store the sentence in the output file.
    #
    # It must close both files when the loop is complete.
    # This must be done by calling the close function.
    for data in infile:
        splitlines = data.split()
        player = splitlines[0] + ' ' + splitlines[1]
        goals = splitlines[2]
        assists = splitlines[3]
        total_points = int(splitlines[2]) + int(splitlines[3])
        sentence = f'In 2019-20 {player} of the LA Kings scored {goals} goals and had {assists} assists for {total_points} points.\n'
        outfile.write(sentence)
    infile.close()
    outfile.close()

def display(show):
    # This function has one parameter for the file
    # whose data is being displayed.
    #
    # It must use a while loop to display each line in the file
    # with no gaps between the lines of output.
    # This while loop must use a test condition containing an actual boolean expression
    # with a comparison operator and not contain break or continue statements.
    #
    # It must close the file when the loop is complete.
    # This must be done by using the close function.
    line = show.readline()
    while line != '':
        line = line.rstrip()
        print(line)
        line = show.readline()
    show.close()

main()