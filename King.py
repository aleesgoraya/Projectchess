from array import *
from ChessPiece import ChessPiece


class King(ChessPiece):
    """
    A class representing a King piece in the chess game on the chess board.
    A king can move in a 3*3 square centred by itself. It is the most important
    piece in the chess game. If it is checkmated, then game is over.
    """

    def __init__(self, color, position) -> None:
        """Initializing a King piece with <color> and <position>.
         """
        super().__init__(color, position)

    def valid_coordinates(self, row, col) -> bool:
        """Return true iff (row, col) is a valid position that the King can
        move to.
        """
        valid = False
        for i in range(-1, 2):
            for j in range(-1, 2):
                if row == self.position[0] + i and col == self.position[1] + j:
                    valid = True
        return valid

