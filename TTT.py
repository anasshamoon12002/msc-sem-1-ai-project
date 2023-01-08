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

    def set_player(self, count):
        pass

    def get_player_mark(self):
        pass

    # Checks if there is a winner based upon the rules of tic tac toe
    def check_winner(self):
        pass

    def check_rows(self):
        for i in range(len(self.board)):
            if self.check_row_and_col(self.board[0][i], self.board[1][i], self.board[2][i]):
                return True
        return False

    def check_columns(self):
        pass

    def check_diagonals(self):
        pass

    # Checks if the values are same and are not empty. Used in checking the rows, columns and diagonals for the winner
    def check_row_and_col(self, val_1, val_2, val_3):
        return val_1 != "   " and val_1 == val_2 and val_2 == val_3


