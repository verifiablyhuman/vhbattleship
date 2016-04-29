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


def player_wins(pboard, sboard):
    pass


def get_guess():
    pass


def check_hit(pboard, sboard):
    pass