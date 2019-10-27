from array import *
from ChessPiece import ChessPiece


class Rook(ChessPiece):

    """position is the current position of rook. row and col given for where the piece should be moved.
       board is a two dimensional array which contains player has what pieces on the board.
       for example at board[1,1] there might be a white piece represented by "W".
       Black piece represented by "B" and empty represented by "E"
    """
    def move(self, position, row, col, board):
        check_position=[]
        if col>position[1]: # Rook moves towards right
            check_position[1] = position[1]+1
            move = "r"

        elif col<position[1]: # Rook moves left
            check_position[1] = position[1] - 1
            move = "l"

        elif row>position[0]: # Rook moves forward
            check_position[0] = position[0] + 1
            move = "f"

        elif row<position[0]: # Rook moves backwards
            check_position[0]=position[0]-1
            move = "b"

        while board[check_position[0]][check_position[1]] == "E":  # check whether every square in between is empty
            if move == "b":
                check_position[0] = position[0] - 1
            elif move == "f":
                check_position[0] = position[0] + 1
            elif move == "l":
                check_position[1] = position[1] - 1
            elif move == "r":
                check_position[1] = position[1] + 1

        if board[check_position[0]][check_position[1]] == self.color:           # check if there is a player
            return False













