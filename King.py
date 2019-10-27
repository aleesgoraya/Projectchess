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

    def check_move(self, row, col, board) -> bool:
        """

        :param row:
        :param col:
        :param board:
        :return:
        """
