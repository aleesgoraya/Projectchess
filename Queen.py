from array import *
from ChessPiece import ChessPiece


class Queen(ChessPiece):

    """Position is the current position of Queen. Row and col is where the piece should be moved.
       The board is a two dimensional array which contains the players and their corresponding piece colour.
       eg. at board[1,1] there might be a white piece represented by "W".
       Black piece represented by "B" and empty represented by "E"
    """

    def __init__(self, colour, position):
        super().__init__(colour, position)



    """Position is the current position of Queen. Row and col is where the piece should be moved.
       The board is a two dimensional array which contains the players and their corresponding piece colour.
       eg. at board[1,1] there might be a white piece represented by "W".
       Black piece represented by "B" and empty represented by "E". Ensures piece is moving to a valid location on
       on the board following its movement capabilities.
    """
    
    def valid_coordinates (self, position, row, col):

        if row<0 or row>7:   #Checks to ensure coordinates are on board
            return False
        if col<0 or col>7:
            return False
        
        rise = row-position[0]
        run = col-position[1]

        if rise == 0 and run ==0: #checks to make sure piece isn't moving to current location 
            return False
        elif rise == 0 or run == 0: #checks to see if piece is moving up/down or side/side
            return True
        elif rise/run == -1 or rise/run ==1: #checks to see if piece is moving diagonally
            return True
        else:
            return False















