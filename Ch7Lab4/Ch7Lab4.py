# Christopher Earl, Chapter 7 Lab 4

def main():
    # Part 1
    with open('misl.txt', 'r') as misl:
        champs, howmany = get_champs(misl)
    for x in range(0, howmany):
        print(champs[x][0], 'won rgw MISL championship in', champs[x][1])
    # Part 2
    premier = ('Liverpool', 'Chelsea', 'Arsenal')
    mls = ('LAFC', 'LA Galaxy', 'St. Louis City SC')
    print('Premier tuple:', end=' ')
    for team in premier:
        print(team, end=' ')
    print()
    print('MLS tuple:', end=' ')
    for x in range(0, len(mls)):
        print(mls[x], end=' ')
    print()
    mls1, mls2, mls3 = mls
    soccer_teams = list(premier)
    soccer_teams.append(mls1)
    soccer_teams.append(mls2)
    soccer_teams.append(mls3)
    print('Soccer Teams List:', soccer_teams)
    soccer_teams = tuple(soccer_teams)
    print('Soccer Teams Tuple:', soccer_teams)
def get_champs(file):
    num = 0
    the_list = []
    team = file.readline().rstrip('\n')
    while team != '':
        year = file.readline().rstrip('\n')
        the_list.append([team, year])   # add a row to the the_list
        num += 1
        team = file.readline().rstrip('\n')
    return the_list, num
main()
