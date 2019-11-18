from Chessboard import Chessboard
from ChessPiece import ChessPiece


class Chess:
    """
    A class representing a chess game.

    ==Private Attribute==
    _board_dimension: the size of the chess board
    _chess_board: the Chessboard class
    _current_turn: the current turn of the chess game
    _number_of_moves: the number of moves has been made
    """

    _board_dimension: int
    _chess_board: Chessboard
    _current_turn: str
    _number_of_moves: int

    def __init__(self) -> None:
        self._board_dimension = 8
        self._chess_board = Chessboard()
        self._current_turn = Chessboard.P1
        self._number_of_moves = 0

    def get_current_turn(self) -> str:
        """Return that player that is currently making a move.
        """
        return self._current_turn

    def get_piece(self, row, col) -> ChessPiece:
        """Return the piece that is at the specified row and column.
        """
        return self._chess_board.get(row, col)

    def get_chess_board(self) -> Chessboard:
        """Return the chess board of this chess game.
        """
        return self._chess_board

    def move(self, row, col) -> None:
        """Make a move with the ChessBoard class and update the Chess Game
        accordingly.
        """
        if self._chess_board.move(row, col):
            self._current_turn = self._chess_board.get_other_player\
                (self._current_turn)
            self._number_of_moves += 1

    def has_check(self, player):
        """Return true if this player's king has been put into check, false
        otherwise
        """
        self._chess_board.has_check(player)

    def has_check_mate(self, player):
        """Return true if this player's king has been put into checkmate,
        false otherwise.
        """
        self._chess_board.has_check_mate(player)

    def get_winner(self):
        """Return the winner of the game.
        """
        if self.is_game_over():
            if self._chess_board.has_check_mate(self._chess_board.P1):
                return self._chess_board.get_other_player(self._chess_board.P1)
            return self._chess_board.P2

    def is_game_over(self):
        """Return whether the game is over.
        """
        if self._chess_board.has_check_mate(self._chess_board.P1) or \
                self._chess_board.has_check_mate(self._chess_board.P2):
            return True
        return False

    # No need for a string representation
    # """
    # Return a string representation of the chess board
    # """
    # def get_chess_board(self):
    #     return self._chess_board.toString()
