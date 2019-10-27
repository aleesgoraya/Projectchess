from array import *
from ChessPiece import ChessPiece


class Pawn(ChessPiece):

    """
    Changes methods to fit that of a pawn. ie valid_coordinates are only up one
    diagonally on the board.
    """

    def __init__(self, colour, position):
        super().__init__(colour, position)

    def valid_coordinates(self, row, col) -> bool:
        """
        Position is the current position of Pawn. Row and col is where the piece
        should be moved. The board is a two dimensional array which contains the
        players and their corresponding piece colour.
        eg. at board[1,1] there might be a white piece represented by "W".
        Black piece represented by "B" and empty represented by "E"
        """

        # Checks to ensure coordinates are on board
        if row < 0 or row > 7:
            return False
        if col < 0 or col > 7:
            return False

        if self.position[0] <= row:  # ensures piece is moving forward
            return False

        rise = row - self.position[0]
        run = col - self.position[1]

        # checks to make sure piece isn't moving to current location
        if rise == 0 and run == 0:
            return False
        # checks to see if piece is moving diagonally
        elif rise/run == -1 or rise/run == 1:
            return True
        else:
            return False


