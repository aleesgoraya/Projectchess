from ChessPiece import ChessPiece


class Player:
    def __init__(self, chess, color):
        self.chess = chess
        self.color = color
        if self.color == "White":
            self.chess_piece = self.chess.chessboard.white
        else:
            self.chess_piece = self.chess.chessboard.black

    def move(self, start_row, start_col, move_position):
        chosen = self.chess.chessboard.board[start_row][start_col]
        if isinstance(chosen, ChessPiece) and chosen in self.chess_piece and \
                move_position in chosen.get_valid_coordinates():
            chosen.move(move_position)

    @staticmethod
    def get_move():
        raise NotImplementedError
