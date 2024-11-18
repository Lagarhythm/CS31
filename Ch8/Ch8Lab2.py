# Christopher Earl, Ch 8 Lab 2

def main():
    digits = 0
    uppercase = 0
    lowercase = 0
    whitespace = 0

    with open('text.txt', 'r') as text:
        data = text.read()

    for ch in data:
        if ch.isdigit():
            digits += 1
        elif ch.islower():
            lowercase += 1
        elif ch.isupper():
            uppercase += 1
        elif ch.isspace():
            whitespace += 1

    print('Number of digits =', digits)
    print('Number of lowercase =', lowercase)
    print('Number of uppercase =', uppercase)
    print('Number of whitespace characters =', whitespace)
    print()

    with open('OneWordMovieTitles.txt', 'r') as titles:
        movies = titles.read()

    # Part 2
    print('Movies in uppercase:', movies.upper())
    print('Movies in lowercase:', movies.lower())
    if movies.startswith('Deliv'):
        print('Looks like Deliverance comes first')
    else:
        print('Deliverance might be here, but not first')
    if movies.endswith('site'):
        print('Looks like Parasite comes last')
    else:
        print('Parasite might be here, but not last')

    jaws = movies.find('Jaws')
    if jaws == -1:
        print('Jaws is not in the string')
    else:
        print('Jaws is at index', jaws, 'in the string')

    movies2 = movies.replace('Babe', 'Aladdin')
    print('After replace:', movies2)

    # Part 3
    me = input('Enter your first, middle, and last name (space between each): ')
    name = me.split()
    print(name[0][0], '.', name[1][0], '.', name[2][0], sep='')

main()
