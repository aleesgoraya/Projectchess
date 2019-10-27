class playerHuman(Player):
    def __init__(self, chess, color):
        super().__init__(chess, color)
        
    def getmove():
        try:
            row = int(input("row position: "))
            col = int(input("col position: "))
        except:
            print("invalid input")
        else:
            moveposition = (row, col)
            return moveposition
