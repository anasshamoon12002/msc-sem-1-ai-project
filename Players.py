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
            print("\nCurrent Game")
            if count % 2 == 0:
                print("\nplayer 1: X")
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
            if count % 2 == 0:
                print("\nPlayer 1 (X) is the winner!!!\n")
            else:
                print("\nPlayer 2 (O) is the winner!!!\n")
            break
        count += 1

        if game.board_check() and not game.check_winner():
            print("\nThis game is a tie!\n")



    def random_computer(self, turn):
        count_computer = turn

        game = TTT()
        game.set_player(count_computer)
        game.display_board()

        while True:

            print("\nCurrent Game")

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
            print("\nThis game is a tie!\n")


    def AI_computer(self):
        pass
