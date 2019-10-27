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

        """check whether every square is empty between rook and point to move. Keep checking until position is reached 
           or a piece found
        """
        while board[check_position[0]][check_position[1]] == "E" and (row != check_position[0] and col != check_position[1]):
            if move == "b":
                check_position[0] = position[0] - 1
            elif move == "f":
                check_position[0] = position[0] + 1
            elif move == "l":
                check_position[1] = position[1] - 1
            elif move == "r":
                check_position[1] = position[1] + 1

        # First check to see if a piece was found in way before reaching position if yes then return false
        # as move cannot be made
        if check_position[0] == row and check_position[1] == col:

            # check if there is already a player piece there then move cannot be made
            if board[check_position[0]][check_position[1]] == self.color:

                return False

            # check if the piece found is for other player. Player can take the piece and assume its position
            if board[check_position[0]][check_position[1]] == "B":

                return True

            return True     # This means that the row and col given was empty so piece can be placed
            
        else:
            return False












