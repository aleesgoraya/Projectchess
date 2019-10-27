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

    def get_valid_coordinates(self) -> list:
        """Return a list of valid moves that the King has.
        """
        ans = []
        current_row, current_col = self.position[0], self.position[1]

        for d_row in range(-1, 2):
            for d_col in range(-1, 2):
                while current_row < 8 and current_col < 8:
                    current_row += d_row
                    current_col += d_col
                    ans.append((current_row, current_col))
        return ans

    def valid_coordinates(self, row, col) -> bool:
        """Return true iff (row, col) is a valid position that the King can
        move to.
        """
        valid = False

        for move in self.get_valid_coordinates():
            if row == move[0] and col == move[1]:
                valid = True

        return valid

