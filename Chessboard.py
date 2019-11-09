from Bishop import Bishop
from King import King
from Knight import Knight
from Pawn import Pawn
from Queen import Queen
from Rook import Rook


class Chessboard:
    """A class representing a chess board for a chess game. A chess board
    is a 8*8 grid.
    """
    def __init__(self) -> None:
        """Initializing a chess board for the chess game.
        """
        self.board = [[], [], [], [], [], [], [], []]
        for row in range(len(self.board)):
            for col in range(0, 8):
                self.board[row].append("")
        self.white = []
        self.black = []
        for col in range(0, 8):
            w_pawn = Pawn("white", (6, col))
            b_pawn = Pawn("black", (1, col))
            self.white.append(w_pawn)
            self.black.append(b_pawn)
            self.board[6][col] = w_pawn
            self.board[1][col] = b_pawn
        w_rook1 = Rook("white", (7, 0))
        w_rook2 = Rook("white", (7, 7))
        w_knight1 = Knight("white", (7, 1))
        w_knight2 = Knight("white", (7, 6))
        w_bishop1 = Bishop("white", (7, 2))
        w_bishop2 = Bishop("white", (7, 5))
        w_queen = Queen("white", (7, 3))
        w_king = King("white", (7, 4))
        brook1 = Rook("black", (0, 0))
        brook2 = Rook("black", (0, 7))
        b_knight1 = Knight("black", (0, 1))
        b_knight2 = Knight("black", (0, 6))
        b_bishop1 = Bishop("black", (0, 2))
        b_bishop2 = Bishop("black", (0, 5))
        b_queen = Queen("black", (0, 3))
        b_king = King("black", (0, 4))
        self.white.append(w_rook1)
        self.white.append(w_rook2)
        self.white.append(w_knight1)
        self.white.append(w_knight2)
        self.white.append(w_bishop1)
        self.white.append(w_bishop2)
        self.white.append(w_queen)
        self.white.append(w_king)
        self.black.append(brook1)
        self.black.append(brook2)
        self.black.append(b_knight1)
        self.black.append(b_knight2)
        self.black.append(b_bishop1)
        self.black.append(b_bishop2)
        self.black.append(b_queen)
        self.black.append(b_king)
        for piece in self.white:
            self.board[piece.get_position()[0]][piece.get_position()[1]] = piece
        for piece in self.black:
            self.board[piece.get_position()[0]][piece.get_position()[1]] = piece




