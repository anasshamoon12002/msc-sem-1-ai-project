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
        if count % 2 == 0:
            self.player_mark = "  X  "
        else:
            self.player_mark = "  O  "

    def get_player_mark(self):
        return self.player_mark

    # Checks if there is a winner based upon the rules of tic tac toe
    def check_winner(self):
        return self.check_rows() or self.check_diagonals() or self.check_columns()

    def check_rows(self):
        for i in range(len(self.board)):
            if self.check_row_and_col(self.board[i][0], self.board[i][1], self.board[i][2]):
                return True
        return False

    def check_columns(self):
        for i in range(len(self.board)):
            if self.check_row_and_col(self.board[0][i], self.board[1][i], self.board[2][i]):
                return True
        return False

    def check_diagonals(self):
        first_diagonal = self.check_row_and_col(self.board[0][0], self.board[1][1], self.board[2][2])
        second_diagonal = self.check_row_and_col(self.board[0][2], self.board[1][1], self.board[2][0])
        return first_diagonal or second_diagonal

    # Checks if the values are same and are not empty. Used in checking the rows, columns and diagonals for the winner
    def check_row_and_col(self, val_1, val_2, val_3):
        return val_1 != "   " and val_1 == val_2 and val_2 == val_3

    def value_check(self, row, column):
        return self.board[row-1][column-1] == "   "

    def modify_board(self, rows, columns):
        if rows > 0 and rows < 4 and columns < 4 and columns > 0:
            if self.board[rows - 1][columns - 1] == "   ":
                self.board[rows - 1][columns - 1] = self.get_player_mark()

