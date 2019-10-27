class Chessboard:
<<<<<<< HEAD
    def __init__(self):
        self.board = [[], [], [], [], [], [], [], []]
        for row in len(self.board):
            for col in (0, 8):
                self.board[row].append('')
        self.white = []
        self.black = []
        for col in (0, 8):
            wpawn = Pawn("white", (6, col))
            bpawn = Pawn("black", (1, col))
            self.white.append(wpawn)
            self.black.append(bpawn)
            self.board[6][col] = wpawn
            self.board[1][col] = bpawn
        wrook1 = Rook("white", (7, 0))
        wrook2 = Rook("white", (7, 7))
        wknight1 = Knight("white", (7, 1))
        wknight2 = Knight("white", (7, 6))
        wbishop1 = Bishop("white", (7, 2))
        wbishop2 = Bishop("white", (7, 5))
        wqueen = Queen("white", (7, 3))
        wking = King("white", (7, 4))
        brook1 = Rook("black", (0, 0))
        brook2 = Rook("black", (0, 7))
        bknight1 = Knight("black", (0, 1))
        bknight2 = Knight("black", (0, 6))
        bbishop1 = Bishop("black", (0, 2))
        bbishop2 = Bishop("black", (0, 5))
        bqueen = Queen("black", (0, 3))
        bking = King("black", (0, 4))
        self.white.append(wrook1)
        self.white.append(wrook2)
        self.white.append(wknight1)
        self.white.append(wknight2)
        self.white.append(wbishop1)
        self.white.append(wbishop2)
        self.white.append(wqueen)
        self.white.append(wking)
        self.black.append(brook1)
        self.black.append(brook2)
        self.black.append(bknight1)
        self.black.append(bknight2)
        self.black.append(bbishop1)
        self.black.append(bbishop2)
        self.black.append(bqueen)
        self.black.append(bking)
        for piece in self.white:
            self.board[piece.position[0]][piece.position[1]] = piece
        for piece in self.black:
            self.board[piece.position[0]][piece.position[1]] = piece
=======
    """A class representing a chess board for a chess game. A chess board
    is a 8*8 grid.
    """

    def __init__(self) -> None:
        """Initializing a chess board for the chess game.
        """
        pass
>>>>>>> 7eb71958b640c019a1a12afbfdc1af42a14994da
