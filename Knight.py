from array import *
from ChessPiece import ChessPiece


class Knight(ChessPiece):
    """position is the current position of Knight. row and col given for where
       the piece should be moved. Board is a two dimensional array which
       contains player has what pieces on the board.
       For example at board[1,1] there might be a white piece represented by "W"
       Black piece represented by "B" and empty represented by "E"
    """

    def get_valid_coordinates(self) -> list:
        """Return a list of valid moves that the Knight has.
        """
        ans = []
        current_row, current_col = self.position[0], self.position[1]
        # A Knight only has 8 possible moves.
        ans.append((current_row - 2, current_col - 1))
        ans.append((current_row - 2, current_col + 1))
        ans.append((current_row - 1, current_col - 2))
        ans.append((current_row - 1, current_col + 2))
        ans.append((current_row + 1, current_col - 2))
        ans.append((current_row + 1, current_col + 2))
        ans.append((current_row + 2, current_col - 1))
        ans.append((current_row + 2, current_col + 1))
        return ans

    def check_move(self, row, col, board) -> bool:
        """Return True iff there is an enemy piece or empty at the (row, col).
        """
        return self.valid_coordinates(row, col) and board[row][col] != \
            self.color


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
board = [["B", "B", "B", "B", "B", "B", "B", "B"],
         ["B", "B", "B", "B", "B", "B", "B", "B"],
         ["E", "E", "E", "E", "E", "E", "E", "E"],
         ["E", "E", "E", "E", "E", "E", "E", "E"],
         ["E", "E", "E", "E", "E", "E", "E", "E"],
         ["E", "E", "E", "E", "E", "E", "E", "E"],
         ["W", "W", "W", "W", "W", "W", "W", "W"],
         ["W", "W", "W", "W", "W", "W", "W", "W"]
         ]
print(p1.check_move(p1.position, 2, 3, board))
