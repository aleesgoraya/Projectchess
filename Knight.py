from array import *
from ChessPiece import ChessPiece


class Knight(ChessPiece):

    """position is the current position of Knight. row and col given for where
       the piece should be moved. Board is a two dimensional array which
       contains player has what pieces on the board.
       For example at board[1,1] there might be a white piece represented by "W"
       Black piece represented by "B" and empty represented by "E"
    """
    def check_move(self, row, col, board):
        check_position = [0, 0]

        # If player's own piece is present then invalid move
        if board[row][col] == self.color:
            return False

        # Knight only has 8 possible moves.
        # Id doesnt matter if position is empty or taken by enemy.
        # Knight will take the position
        if row == self.position[0]+2 and col == self.position[1]+1:
            return True
        elif row == self.position[0]+2 and col == self.position[1]-1:
            return True
        elif row == self.position[0]+1 and col == self.position[1]+2:
            return True
        elif row == self.position[0]+1 and col == self.position[1]-2:
            return True
        elif row == self.position[0]-1 and col == self.position[1]+2:
            return True
        elif row == self.position[0]-1 and col == self.position[1]-2:
            return True
        elif row == self.position[0]-2 and col == self.position[1]+1:
            return True
        elif row == self.position[0]-2 and col == self.position[1]-1:
            return True

        return False


if __name__ == "__main__":

    """
    Board will be represented the following way in 2-d array
         7  "W" "W","W","W","W","W","W","W"  
         6  "W","W","W","W","W","W","W","W"     
         5  "E","E","E","E","E","E","E","E"  
         4  "E","E","E","E","E","E","E","E"  
         3  "E","E","E","E","E","E","E","E"  
         2  "E","E","E","E","E","E","E","E"  
         1  "B","B","B","B","B","B","B","B"  
         0  "B","B","B","B","B","B","B","B"  
             0   1   2   3   4   5   6   7
    """

    """
    Testing out the class
    """

p1 = Knight("B", [4, 3])
board = [["B","B","B","B","B","B","B","B"],
         ["B","B","B","B","B","B","B","B"],
         ["E","E","E","E","E","E","E","E"],
         ["E","E","E","E","E","E","E","E"],
         ["E","E","E","E","E","E","E","E"],
         ["E","E","E","E","E","E","E","E"],
         ["W","W","W","W","W","W","W","W"],
         ["W","W","W","W","W","W","W","W"]
         ]
print(p1.check_move(p1.position, 2, 3, board))










