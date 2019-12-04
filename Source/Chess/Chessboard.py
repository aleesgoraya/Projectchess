from Chess.Bishop import Bishop
from Chess.King import King
from Chess.Knight import Knight
from Chess.Pawn import Pawn
from Chess.Queen import Queen
from Chess.Rook import Rook
from Chess.ChessPiece import ChessPiece


class Chessboard:
    """A class representing a chess board for a chess game. A chess board
    is a 8*8 grid.

    ==Attribute==
    P1: player 1 who play white chess pieces
    P2: player 2 who play black chess pieces
    board: a list that represents the board
    white: a list consists of all the white chess pieces
    black: a list consists of all the black chess pieces
    """

    P1: str
    P2: str
    board: list
    white: list
    black: list

    def __init__(self) -> None:
        """Initializing a chess board for the chess game.
        """
        self.P1 = "white"
        self.P2 = "black"
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

    def get_other_player(self, player: str) -> str:
        """Return the other player who is playing
        against <player>
        """
        if player == self.P1:
            return self.P2
        else:
            return self.P1

    def get(self, row: int, col: int) -> ChessPiece:
        """Get the ChessPiece with given <row> and
        <col>.
        """
        return self.board[row][col]

    def return_p1(self) -> str:
        return self.P1

    def return_p2(self) -> str:
        return self.P2

    def move(self, row: int, col: int) -> bool:
        """Return true if and only if the move is successfully made.
        """
        pass

    def has_check(self, player: str) -> bool:
        """Return true if and only if the <player> 's king is in check.
        """
        pass

    def has_check_mate(self, player: str) -> bool:
        """Return true if and only if the <player> 's king is in check mate.
        """
        pass

