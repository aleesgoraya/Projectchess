from abc import ABC, abstractclassmethod


class ChessPiece(ABC):

    # position is an array containing row and col e.g [0,1] 0 is row and 1 is col
    def __init__(self, color, position):
        self.color = color
        self.position = position
        super().__init__()

    def return_color(self):
        return self.color

    def return_position(self):
        return self.position


    '''
    checks to see if there are any pieces between starting position and position
    the piece is being moved to. Position is the starting position of the piece,
    (row,col) is the desired position, and board is the board being used. 

    '''
    def checkMove(self, position, row, col, board):

        if not validCoordinates(position, row, col):
            return False
        
        r = False
        l = False
        f = False
        b = False
        
        check_position=[position[0], position[1]]
        if col>position[1]: # Piece moves right
            check_position[1] += 1
            r = True

        elif col<position[1]: # Piece moves left
            check_position[1] += - 1
            l = True

        elif row>position[0]: # Pice moves forward
            check_position[0] += 1
            f = True

        elif row<position[0]: # Piece moves backwards
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
