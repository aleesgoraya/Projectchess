from array import *

from ChessPiece import ChessPiece


class Rook(ChessPiece):
    """
       position is the current position of rook. row and col given for where
       the piece should be moved.
       board is a two dimensional array containing which players
       have what pieces on the board.
       for example
       at [1,1] there might be a white piece represented by "W".
       At [2,1] there might be a Black piece represented by "B"
       At [3,1] empty represented by "E"
    """

    def check_move(self, position, row, col, board):

        check_position = [0, 0]

        # Rook moves right Column changes(increases) row doesnt
        if col > position[1]:

            check_position[1] = position[1] + 1
            check_position[0] = position[0]
            move = "r"

        # Rook moves left Column changes(decreases) row doesnt
        elif col < position[1]:

            check_position[1] = position[1] - 1
            check_position[0] = position[0]
            move = "l"

        # Rook moves forward row changes(increases) Column doesnt
        elif row > position[0]:

            check_position[0] = position[0] + 1
            check_position[1] = position[1]
            move = "f"

        # Rook moves backwards row changes(decreases) Column doesnt
        elif row < position[0]:

            check_position[0] = position[0] - 1
            check_position[1] = position[1]
            move = "b"

        """check whether every square is empty between rook and point to move. 
           Keep checking until position is reached 
           or a piece found"""
        while board[check_position[0]][check_position[1]] == "E" and (
                row != check_position[0] or col != check_position[1]):

            if move == "b":
                check_position[0] = check_position[0] - 1
            elif move == "f":
                check_position[0] = check_position[0] + 1
            elif move == "l":
                check_position[1] = check_position[1] - 1
            elif move == "r":
                check_position[1] = check_position[1] + 1

        # First check to see if a piece was found in way before reaching
        # position if yes then return false as move cannot be made
        if check_position[0] == row and check_position[1] == col:

            # check if there is already a player piece there then move
            # cannot be made
            if board[row][col] == self.color:

                return False

            # check if the piece found is for other player
            # Player can take the piece and assume its position
            if board[row][col] == "B":

                return True

            return True  # This means that the row and col given was empty
                          # so piece can be placed
        else:
            
            return False


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
board = [["B", "B", "B", "B", "B", "B", "B", "B"],
         ["B", "B", "B", "B", "B", "B", "B", "B"],
         ["E", "E", "E", "E", "E", "E", "E", "E"],
         ["E", "E", "E", "E", "E", "E", "E", "E"],
         ["E", "E", "E", "E", "E", "E", "E", "E"],
         ["E", "E", "E", "E", "E", "E", "E", "E"],
         ["W", "W", "W", "W", "W", "W", "W", "W"],
         ["W", "W", "W", "W", "W", "W", "W", "W"]
         ]
print(p1.check_move(p1.position, 1, 6, board))
