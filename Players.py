from TTT import TTT

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
                print("\nplayer 1: x")
            game.set_player(count)
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
                print("\nPlayer 1 (x) is the winner!!!\n")
            else:
                print("\nPlayer 2 (o) is the winner!!!\n")
            break
        count += 1



    def random_computer(self):
        pass

    def AI_computer(self):
        pass
