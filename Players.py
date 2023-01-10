from TTT import TTT
import random

class Players:
    def __init__(self):
        self.row = 0
        self.column = 0

    def multiplayer(self, num):
        count = num
        game = TTT()
        while True:
            if game.board_check():
                break

            print("\nCurrent Game")
            if count % 2 == 0:
                print("\nPlayer 1: X")
            else:
                print("\nPlayer 2: O")
            game.set_player(count)
            game.display_board()
            while True:
                self.row = int(input("Enter number of row: "))
                self.column = int(input("Enter number of column: "))
                if game.value_check(self.row, self.column) and self.row > 0 and self.row < 4 and self.column > 0 and self.column < 4:
                    game.modify_board(self.row, self.column)
                    break
                else:
                    print("\nWrong Input!!!Try again!!! \n")
            if game.check_winner():
                print()
                game.display_board()
                if count % 2 == 0:
                    print("\nPlayer 1 (X) is the winner!!!\n")
                else:
                    print("\nPlayer 2 (O) is the winner!!!\n")
                break
            count += 1

        print(game.board_check(), game.check_winner())

        if game.board_check() and not game.check_winner():
            game.display_board()
            print("\nThis game is a tie!\n")



    def random_computer(self, turn):
        count_computer = turn

        game = TTT()

        while True:

            if game.board_check():
                break

            print("\nCurrent Game")
            game.set_player(count_computer)
            game.display_board()

            if count_computer % 2 == 0:
                print("\nYou: X")
                self.row = int(input("Enter number of row: "))
                self.column = int(input("Enter number of column: "))
                if self.row > 0 and self.row < 4 and self.column > 0 and self.column < 4 and game.value_check(self.row,
                                                                                                              self.column):
                    game.modify_board(self.row, self.column)

                else:
                    print("\nWrong Input!!! Try again!!! \n")

            else:
                print("\nComputer: 0")
                while True:
                    self.row = random.randint(1, 3)
                    self.column = random.randint(1, 3)

                    if game.value_check(self.row, self.column):
                        game.modify_board(self.row, self.column)
                        break

            if game.check_winner():
                print()
                game.display_board()

                if count_computer % 2 == 0:
                    print("\nYou (X) are the winner!!! \n")
                else:
                    print("\nComputer (0) is the winner!!! \n")

                break

            count_computer += 1

        if game.board_check() and not game.check_winner():
            game.display_board()
            print("\nThis game is a tie!\n")


    def AI_computer(self, turn):
        count_computer = turn
        game = TTT()

        while True:
            if game.board_check():
                break

            print("\nCurrent Game")
            game.set_player(count_computer)
            game.display_board()

            if count_computer % 2 == 0:
                print("\nYou: X")
                while True:
                    self.row = int(input("Enter number of row: "))
                    self.column = int(input("Enter number of column: "))

                    if game.value_check(self.row, self.column) and self.row > 0 and self.row < 4 and self.column > 0 and self.column < 4:
                        game.modify_board(self.row, self.column)
                        break
                    else:
                        print("\nWrong input!!! Try again!\n")
            else:
                print("\nComputer: O")

                # minimax algorithm

            if game.check_winner():
                print()
                game.display_board()
                if count_computer % 2 == 0:
                    print("\nYou (X) are the winner!!")
                else:
                    print("\nComputer (O) is the winner!!")

                break

            count_computer += 1

        if game.board_check() and not game.check_winner():
            game.display_board()
            print("\nThis game is a tie!\n")


    def evaluate(self, b, player, opponent):

        #checking for row for X or O victory.
        for row in range(3):
            if(b[row][0] == b[row][1] and b[row][1] == b[row][2]):
                if (b[row][0] == player):
                    return 10
                elif (b[row][0] == opponent):
                    return -10

        #checking for columns for X or O victory.
        for col in range(3):
            if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):
                if (b[0][col] == player):
                    return 10
                elif (b[0][col]== opponent):
                    return -10
        #checking for Diagonals for X or O victory.
        if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):

            if (b[0][0] == player):
                return 10
            elif (b[0][0] == opponent):
                return -10

        if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):

              if (b[0][2] == player):
                  return 10
              elif (b[0][2] == opponent):
                  return -10
        #Else isMovesLeft(self, board):
        return 0
    
    def isMovesLeft(self, board):
        for i in range(3):
            for J in range(3):
                if (board[i][j] == '   '):
                    return True
        return False

    def minimax(self, board, depth, isMax, player, opponent):
        score = self.evaluate(board, player, opponent)

        #if Maximizer has won the game return his\her
        #evaluated score
        if (score == 10):
            return score

        #if Minimizer has won the game return his\her
        #evaluated score
        if (score == -10):
            return score
        #if there are no more moves and no winner then
        #it is a tie
        if (self.isMovesLeft(board) == False):
            return 0
        #if this maximizer's move
        if (isMax):
            best = -1000

            #traverse all cells
            for i in range(3):
                for J in range(3):

                    #check if cell is empty
                     if (board[i][j] == '   '):
                         #Make the move
                         board[i][j] = player

                         #call minimax recursively and choose
                         #the maximum value
                         best = max(best, self.minimax(board, depth + 1, not isMax, player, opponent))
                         #Undo the move
                         board[i][j] = '   '
            return best
        #if this minimizer's move
        else:
            best = 1000
            #Traverse all cells
            for i in range(3):
                for j in range(3):

                    #Check if cell is empty
                    if (board[i][j] == '   '):
                         #Make the move
                         board[i][j] = opponent

                         #call minimax recursively and choose
                         #the minimum value
                         best = min(best, self.minimax(board, depth + 1, not isMax, player, opponent))

                         #undo the move
                         board[i][j] = '   '
            return best










