from array import *
from ChessPiece import ChessPiece


class Queen(ChessPiece):

    """A class representing the Queen piece on chess board in this chess game.
    A Queen can move any number of steps in a straight line horizontally,
    vertically and diagonally if there's no other pieces in her way.
    """

    def __init__(self, colour, position):
        super().__init__(colour, position)

    def valid_coordinates(self, row, col) -> bool:
        """Position is the current position of Queen. Row and col is where the
        piece should be moved. The board is a two dimensional array which
        contains the players and their corresponding piece colour.
        eg. at board[1,1] there might be a white piece represented by "W".
        Black piece represented by "B" and empty represented by "E".
        Ensures piece is moving to a valid location on the board following
        its movement capabilities.
        """

        # Checks to ensure coordinates are on board
        if row < 0 or row > 7:
            return False
        if col < 0 or col > 7:
            return False

        rise = row-self.position[0]
        run = col-self.position[1]

        # checks to make sure piece isn't moving to current location
        if rise == 0 and run == 0:
            return False

        # checks to see if piece is moving up/down or side/side
        elif rise == 0 or run == 0:
            return True

        # checks to see if piece is moving diagonally
        elif rise/run == -1 or rise/run == 1:
            return True
        else:
            return False















