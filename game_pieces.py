"""This module contains the classes for the battleship game."""

from random import choice
from game_methods import get_spots, invert


class Board:

    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    def __init__(self, hdim, vdim):
        """This function creates a basic initial board."""
        self._board = []
        self._num_row = [str(x) for x in xrange(hdim)]
        for a in xrange(vdim):
            self._board.append([])
            for b in xrange(hdim):
                self._board[a].append('O')

    def print_board(self):
        """This function prints the board in its current state."""
        print '  ' + ' '.join(self._num_row)
        for c, row in zip(Board.alpha, self._board):
            print c, ' '.join(row)

    def get_board(self):
        """This function returns the actual board of the board object."""
        return self._board

    def place_ship(self, pos):
        """This function takes a position tuple of a ship and puts it on the board."""
        row, col, orientation, size = pos

        if orientation == 0:
            for a in xrange(size):
                self._board[row][col + a] = 'S'
        else:
            for b in xrange(size):
                self._board[row + b][col] = 'S'

    def add_guess(self, guess):
        row, col = guess
        try:
            if self._board[row][col] != 'O':
                print "You already guessed that. Try again."
                return False
            else:
                self._board[row][col] = 'G'
                return True
        except IndexError:
            print "That's not on the board. Try again."
            return False


class Ship:
    
    def __init__(self, board, size):
        """This function takes a board with ships on it, finds valid locations on the board
         for a ship, and chooses a location a new ship randomly.
        """
        self._board = []
        self._choices = []

        # Loop through to get an initial idea of where the ship could go.
        for a, row in enumerate(board):
            self._board.append([])
            for col in row:
                if col != 'S':
                    self._board[a].append(True)
                else:
                    self._board[a].append(False)

        # Loop through the rows to see what possible positions there are in rows.
        for a, row in enumerate(self._board):
            self._row_spots = get_spots(row, size)
            for b, col in enumerate(self._row_spots):
                if all(col):
                    self._choices.append((a, b, 0, size))

        # Loop through the columns to see what possible positions they hold.
        for a, col in enumerate(invert(self._board)):
            self._col_spots = get_spots(col, size)
            for b, row in enumerate(self._col_spots):
                if all(row):
                    self._choices.append((b, a, 1, size))

        # Pick one of the possible choices.
        self._choice = choice(self._choices)

    def get_pos(self):
        """This function returns the position of the ship. It should give a tuple of the form
        (row, col, orientation)."""
        return self._choice
