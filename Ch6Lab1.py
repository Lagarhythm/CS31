# Christopher Earl, Ch 6, Lab 1
def main():
    # Part 2 and 3
    outfile = open('players.txt', 'w')
    outfile.write('Sydney Crosby\n')
    outfile.write('John Carlson\n')
    outfile.write('Jordan Binnington\n')
    outfile.close()

    outfile = open('players.txt', 'a')
    outfile.write('Alex Ovechkin\n')
    outfile.close()

    outfile = open('numbers.txt', 'w')
    outfile.write(str(89) + '\n')
    outfile.write(str(74) + '\n')
    outfile.write(str(50) + '\n')
    outfile.write(str(8) + '\n')
    outfile.close()

    # infile1 = open('players.txt', 'r')
    # infile2 = open('numbers.txt', 'r')

    with (open('players.txt', 'r') as infile1,
          open('numbers.txt', 'r') as infile2):
        for player in infile1:
            num = infile2.readline().rstrip('\n')
            print(player.strip(), 'wears number', num)

    # player1 = infile1.readline().rstrip('\n')
    # player2 = infile1.readline().rstrip('\n')
    # player3 = infile1.readline().rstrip('\n')
    # player4 = infile1.readline().rstrip('\n')

    # num1 = infile2.readline().rstrip('\n')
    # num2 = infile2.readline().rstrip('\n')
    # num3 = infile2.readline().rstrip('\n')
    # num4 = infile2.readline().rstrip('\n')

    # print(player1, 'wears number', num1)
    # print(player2, 'wears number', num2)
    # print(player3, 'wears number', num3)
    # print(player4, 'wears number', num4)

    # infile1.close()
    # infile2.close()


main()