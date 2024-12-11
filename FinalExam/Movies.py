class Movies:
    def __init__(self, year, title):
        # - Create private variables for the year and title of a movie.
        #   NOTE: These variables must be private.
        # - Set the initial value of these variables to their respective arguments.
        self.__year = year
        self.__title = title

    def __str__(self):
        # - This function must use an f-string to return a string containing
        #   the values of the two private variables in a sentence (see sample output).
        return self.__title + ' debuted in ' + self.__year

def main():
    m = []
    # - Open the movies.txt file for reading (with statement recommended)
    #
    # - Within this with statement, do the following:
    #    - Read the year for the current movie, using rstrip to remove the '\n' character.
    #    - Within a while loop, do the following:
    #        - Read the title of the current monument, using rstrip to remove the '\n' character.
    #        - Create an object of the Movies class using the year and title values that have
    #          been read and use the append function to add this object to the list named m.
    #        - Read the year for the next movie, using rstrip to remove the '\n' character.
    #
    # - When the with statement is finished, use a for loop to print the data for each object
    #   in the list named m in sentences.

    with open('movies.txt', 'r') as inputfile:
        year = inputfile.readline()
        m = []
        while year != '':
            year = year.rstrip()
            title = inputfile.readline().rstrip()
            movies = Movies(year, title)
            m.append(movies)
            year = inputfile.readline()

        for data in m:
            print(data)

    print('Submitted by Christopher Earl')

main()