from array import *
from ChessPiece import ChessPiece


class Queen(ChessPiece):

    """A class representing the Queen piece on chess board in this chess game.
    A Queen can move any number of steps in a straight line horizontally,
    vertically and diagonally if there's no other pieces in her way.
    """

    def __init__(self, colour, position):
        super().__init__(colour, position)

    def get_valid_coordinates(self) -> list:
        """Return a list of valid moves that the Queen has.
        """
        ans = []
        current_row, current_col = self.position[0], self.position[1]

        for d_row in range(-1, 2):
            for d_col in range(-1, 2):
                while 0 <= current_row < 8 and 0 <= current_col < 8:
                    current_row += d_row
                    current_col += d_col
                    ans.append((current_row, current_col))

        # this is not a valid move
        ans.remove((self.position[0], self.position[1]))

        return ans













