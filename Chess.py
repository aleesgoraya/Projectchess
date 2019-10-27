import Projectchess.Chessboard

class Chess:
    """
    A class representing a chess game.
    """

    def __init__(self) -> None:
        self.boardDimension = 8
        self.chessBoard = Projectchess.Chessboard(self.boardDimension)
        self.currentTurn= Projectchess.Chessboard.P1
        self.numberOfMoves = 0

    """
    Return that player that is currently making a move
    """
    def getCurrentTurn(self):
        return self.currentTurn

    """
    Return the piece that is at the specified row and column
    """
    def getPiece(self, row, col):
        return self.chessBoard.get(row, col)

    """
    Make a move with the ChessBoard class and update the Chess Game accordingly
    """
    def move(self, row, col):
        self.chessBoard.move()
        self.currentTurn = self.chessBoard.otherPlayer(self.currentTurn)
        self.numberOfMoves += 1



    """
    Return true if this player's king has been put into check, false otherwise
    """
    def hasCheck(self, player):
        self.chessBoard.hasCheck(player)

    """
    Return true if this player's king has been put into checkmate, false otherwise
    """
    def hasCheckMate(self, player):
        self.chessBoard.hasCheckMate(player)

    """
    Return the winner of the game
    """
    def getWinner(self):
        if Chess.isGameOver():
            if self.chessBoard.hasCheckMate(self.chessBoard.P1):
                return self.chessBoard.otherPlayer(self.chessBoard.P1)
            return self.chessBoard.P2

    """
    Return whether the game is over
    """
    def isGameOver(self):
        if self.chessBoard.hasCheckMate(self.chessBoard.P1) or self.chessBoard.hasCheckMate(self.chessBoard.P2):
            return True
        return False

    """
    Return a string representation of the chess board
    """
    def getChessBoard(self):
        return self.chessBoard.toString();
