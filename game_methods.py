"""This module defines some basic methods to be used in BattleShip."""

from math import ceil, floor

def get_lim_input(msg, lower_limit, upper_limit):
    
    bad_input = True
    ll = int(floor(lower_limit))
    ul = int(ceil(upper_limit))
    ans = 0
    
    while bad_input:
        print msg
        ans = int(raw_input('\t> '))
        if ans in range(ll, ul + 1):
            bad_input = False
        else:
            print '\tBad input. Please try again.'
            bad_input = True

    return ans


def get_spots(line, size):
    """This function will split the given line into lists of consecutive elements with the
    length of size."""
    spots = []
    places_to_check = len(line) - size + 1  # what places in a line can fit a ship
    for a in xrange(places_to_check):
        spots.append([line[b] for b in xrange(a, a + size)])
    return spots


def invert(board):
    """This function will switch the rows and columns of the given board."""
    inverted = []
    for a in xrange(len(board[0])):
        inverted.append([row[a] for row in board])
    return inverted


def player_wins(pboard, sboard):
    """This function tests the player board and ship board to see if the player has won."""
    for prow, srow in zip(pboard, sboard):
        for pcell, scell in zip(prow, srow):
            if scell == 'S' and pcell != 'H':
                return False
    else:
        return True


def get_guess():
    print "Guess a place on the board. For row B, column 1 you would guess 'B1'."
    raw_guess = raw_input("\t>")
    char_int_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    row = char_int_map[raw_guess[0]]
    col = int(raw_guess[1])
    return (row, col)


def check_hit(guess, pboard, sboard):
    row, col = guess
    if sboard[row][col] == 'S':
        pboard[row][col] = 'H'
        print 'HIT!'
    else:
        pboard[row][col] = 'X'
        print 'MISS!'
