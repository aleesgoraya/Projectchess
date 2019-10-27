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



    '''
    Checks to ensure that specifics coordinates are a valid location on the board, and that it moves as expected by the piece.

    '''
    def validCoordinates (self, position, row, col):

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

        
    '''
    Checks to see if move to (row,col) on a given board is valid. Assumes all coordinates are valid locations on
    the board and that the move entered is valid for the piece

    '''
    def checkMove(self, position, row, col, board):

        if not validCoordinates(position, row, col):
            return False
        
        r = False
        l = False
        f = False
        b = False
        
        check_position=[position[0], position[1]]
        if col>position[1]: # Queen moves right
            check_position[1] += 1
            r = True

        elif col<position[1]: # Queen moves left
            check_position[1] += - 1
            l = True

        elif row>position[0]: # Queen moves forward
            check_position[0] += 1
            f = True

        elif row<position[0]: # Queen moves backwards
            check_position[0] += -1
            b = True

        while board[check_position[0]][check_position[1]] == "E" and check_position[0]<row and check_position[1]<col:  # check whether every square in between is empty
            if l == True:
                check_position[1] += - 1
            if r == True:
                check_position[1] += 1
            if f == True:
                check_position[0] += 1
            if b == True:
                check_position[0] += -1
                                        :           
        return board[check_position[0]][check_position[1]] == 'E'
    # checks the location where the while loop stopped - either the place the piece wants to move, or somewhere inbetween where there is a piece.
 














