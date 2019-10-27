class Player:
    def __init__(self, chess, color):
        self.chess = chess
        self.color = color
        if self.color == "White":
            self.chess_piece = self.chess.chessboard.white
        else:
            self.chess_piece = self.chess.chessboard.black

    def move(self, startrow, startcol, moveposition):
        chosen = self.chess.chessboard.board[startrow][startcol]
        if isinstance(chosen, ChessPiess) and chosen in self.chess_piece and moveposition in chosen.get_valid_coordinates():
            chosen.move(moveposition)

    def getmove():
        raise NotImplementedError
