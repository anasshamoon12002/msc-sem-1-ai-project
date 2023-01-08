class TTT:
    def __init__(self):
        self.board = [["" for j in range (3)] for i in range(3)]
        self.player_mark = ""
        self.initialize_board()

    def initialize_board(self):
       for i in range(len(self.board)):
          for j in range(len(self.board[i])):

                 self.board[i][j] = "   "

    def display_board(self):
        print("--------------------")
        for i in range(3):
            print("| ", end="")
            for j in range(3):
                print(self.board[i][j] + " | ", end="")
            print()
            print("--------------------")
