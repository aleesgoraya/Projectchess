from Chess import ChessPiece
from Chess import Chess


class Player:
    """This is a class representing the Player in the chess game.

    ==Attribute==
    chess: the chess model
    color: either white or black
    chess_piece: a list that has all the chess pieces in it
    """
    chess: Chess
    color: str
    chess_piece: list

    def __init__(self, chess, color):
        self.chess = chess
        self.color = color
        if self.color == "White":
            self.chess_piece = self.chess.get_chess_board().white
        else:
            self.chess_piece = self.chess.get_chess_board().black

    def move(self, start_row, start_col, move_position):
        chosen = self.chess.get_chess_board().board[start_row][start_col]
        if isinstance(chosen, ChessPiece) and chosen in self.chess_piece and \
                move_position in chosen.get_valid_coordinates():
            chosen.move(move_position)

    def get_move(self):
        raise NotImplementedError
