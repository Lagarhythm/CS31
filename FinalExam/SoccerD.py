def main():
    soccer = {}
    # Add code in main() for this program. No other functions are allowed.
    #
    # Using a with statement, open the soccer.txt file and
    # use input for the file object name.
    #
    # Within the with statement, use a while loop to populate
    # the soccer dictionary as follows:
    # - The names of the players will be the keys. Be sure the
    #   newline character is removed from each key.
    # - The value for each key will be a list containing the number of games the player played,
    #   the number of goals the player scored, and the number of assists the player had (in that order).
    # - The while loop must have a boolean expression with a
    #   comparison operator. Break and continue statements are not allowed.
    #
    # After the with statement, use a for loop to display the data in the
    # dictionary in sentences that match the sample output.
    #
    # Add a line of output that displays your first and last name.
    # Example: Submitted by Kyle Muldrow (use YOUR first and last name)

    with open('soccer.txt', 'r') as input:
        soccer = {}
        player = input.readline()
        while player != '':
            player = player.rstrip()
            soccer_data = input.readline()
            soccer_split = soccer_data.split()
            soccer[player] = [soccer_split]
            player = input.readline()

    for player in soccer:
        print(f'In {soccer[player][0][0]} NASl games, {player} scored {soccer[player][0][1]} goals and {soccer[player][0][2]} assists.')

    print('Submitted by Christopher Earl')

main()