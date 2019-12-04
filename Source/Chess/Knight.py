from Chess.ChessPiece import ChessPiece


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
        current_position = self.get_position()
        current_row, current_col = current_position[0], current_position[1]
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
            self.get_color()
