"""This module is the main operation for the battleship game."""

from game_pieces import Board, Ship
from game_methods import get_lim_input, player_wins, get_guess, check_hit
from math import ceil

print 'Hello. Welcome to BattleShip.'
print 'First, a few questions:'

hdim = get_lim_input('\tHow wide do you want the board to be (2-10 columns)?', 2, 10)
vdim = get_lim_input('\tHow tall do you want the board to be (2-10 rows)?', 2, 10)
player_board = Board(hdim, vdim)
ship_board = Board(hdim, vdim)
board_area = vdim*hdim
min_dim = min(vdim, hdim)

print 'Alright, here is your board:'
player_board.print_board()

print "Now let's determine how many ships there will be."
len_ships = get_lim_input('\tHow long do you want the ships to be (must fit on board)?',
                          1, min_dim)
max_ships = (board_area/2.0) / len_ships
num_ships = get_lim_input('\tHow many ships do you want (1-5 ships, covering less than \
                          half of the board)?', 1, min(5, max_ships))
print 'Your board will have {} ships that are {} tiles long.'.format(num_ships, len_ships)
print "Finally, we'll determine how many turns you get."

min_turns = len_ships * num_ships
ship_prop = (len_ships*num_ships*1.0) / board_area
# max_turns comes from a linear equation based on the inverse of ship_prop.
# This equation is designed to allow more turns if ships make up a lower proportion
# of the board. The lowest value 1/ship_prop can have is about 2, based on rules 
# given to the player. In this case, the player can have guesses for half the board
# and half of min_dim. The highest value 1/ship_prop can have is the board area. In
# this case, the player can have guesses for the entire board, minus min_dim. These
# conditions lead to the given linear equation below. Play testing may alter this.
max_turns = (1.0/ship_prop) * ((0.5*board_area - 1.5*min_dim)/(board_area-2)) + \
            (0.5*board_area - 1 + (0.5 + 3/(board_area-2))*min_dim - 2/(board_area-2))
turns = get_lim_input('\tHow many turns would you like ({}-{} turns)?'.format(min_turns,
                      int(ceil(max_turns))), min_turns, max_turns)
print 'Okay, you will have {} guesses.'.format(turns)
print "Let's get started."

# We need to actually place the ships on their board.
ships = []
for a in xrange(num_ships):
    ships.append(Ship(ship_board.get_board(), len_ships))
    ship_pos = ships[a].get_pos()
    print ship_pos
    ship_board.place_ship(ship_pos)
    ship_board.print_board()

"""# Now we go into the main loop for guessing.
for b in xrange(turns):
    if player_wins(player_board, ship_board):
        print 'Congratulations, you win!'
        break
    else:
        guess = get_guess()
        player_board.add_guess(guess)
        check_hit(player_board, ship_board)
        ship_board.add_guess(guess)
else:
    if player_wins(player_board, ship_board):
        print 'Congratulations, you win!'
    else:
        print "Sorry, you're out of turns.\nGAME OVER"""
    