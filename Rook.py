from array import *
from ChessPiece import ChessPiece


class Rook(ChessPiece):

    def check_move(self, row, col, board):
        check_position = [0, 0]

        # Rook moves towards right
        if col > self.position[1]:
            check_position[1] = self.position[1]+1
            check_position[0] = self.position[0]
            move = "r"

        # Rook moves left
        elif col < self.position[1]:
            check_position[1] = self.position[1] - 1
            check_position[0] = self.position[0]
            move = "l"

        # Rook moves forward
        elif row > self.position[0]:
            check_position[0] = self.position[0] + 1
            check_position[1] = self.position[1]
            move = "f"

        # Rook moves backwards
        elif row < self.position[0]:
            check_position[0] = self.position[0]-1
            check_position[1] = self.position[1]
            move = "b"

        print(check_position[0])
        print(check_position[1])

        """check whether every square is empty between rook and point to move. 
        Keep checking until position is reached 
        or a piece found
        """
        while board[check_position[0]][check_position[1]] == "E" and \
                (row != check_position[0] or col != check_position[1]):
            if move == "b":
                check_position[0] = check_position[0] - 1
            elif move == "f":
                check_position[0] = check_position[0] + 1
            elif move == "l":
                check_position[1] = check_position[1] - 1
            elif move == "r":
                check_position[1] = check_position[1] + 1

        # First check to see if a piece was found in way before reaching
        # position if yes then return false
        # as move cannot be made
        if check_position[0] == row and check_position[1] == col:
            # check if there is already a player piece there
            # then move cannot be made
            if board[row][col] == self.color:
                return False

            # check if the piece found is for other player.
            # Player can take the piece and assume its position
            if board[row][col] == "B":

                return True

            # This means that the row and col given was empty
            # so piece can be placed
            return True

        else:
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
p1 = Rook("B", [5, 6])
board = [["B","B","B","B","B","B","B","B"],
         ["B","B","B","B","B","B","B","B"],
         ["E","E","E","E","E","E","E","E"],
         ["E","E","E","E","E","E","E","E"],
         ["E","E","E","E","E","E","E","E"],
         ["E","E","E","E","E","E","E","E"],
         ["W","W","W","W","W","W","W","W"],
         ["W","W","W","W","W","W","W","W"]
         ]
print(p1.check_move(p1.position, 1, 6, board))










