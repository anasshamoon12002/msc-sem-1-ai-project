
from Players import Players

# def test_multiplayer():
#     play = Players()
#     play.multiplayer(0)
#
# # 0 is for human first 1 is for computer first
# def test_computer(turn):
#     play = Players()
#     play.random_computer(turn)
#
#
# def ai_computer(turn):
#     play = Players()
#     play.AI_computer(turn)
#
# # test_multiplayer()
#
# # test_computer(0)
#
# # test_computer(1)
#
# ai_computer(1)

play = Players()

print("\nTic Tac Toe")
print("\nSCALE \nRows:     1 - 3 \nColumns:  1 - 3")

while True:
    while True:
        try:
            print("\nSelect one option:")
            print("1. Multiplayer   2. Computer (Random Values)   3. Computer (AI)")
            choice = int(input())
            break
        except:
            print("\nWrong or Invalid Input!!! Please try again.")
            # continue


    if choice == 1:
        play.multiplayer(0)
    elif choice == 2 or choice == 3:
        while True:
            try:
                print("\nWho should play first?")
                print("1. Player   2. Computer")
                turn = int(input())
                if not (turn == 1 or turn == 2):
                    print("\nWrong or Invalid Input!!! Please try again.")
                    continue
                break
            except:
                print("\nWrong or Invalid Input!!! Please try again.")

        turn_num = 0 if turn == 1 else 1

        if choice == 2:
            if turn == 1:
                play.random_computer(turn_num)
            else:
                play.random_computer(turn_num)
        else:
            if turn == 1:
                play.AI_computer(turn_num)
            else:
                play.AI_computer(turn_num)

        while True:
            try:
                print("Do you want to play again?")
                print("1. Yes   2. No")
                continue_status = int(input())
                if not (continue_status == 1 or continue_status == 2):
                    print("\nWrong or Invalid Input!!! Please try again.\n")
                    continue
                break
            except:
                print("\nWrong or Invalid Input!!! Please try again.\n")

        if continue_status == 2:
            break


    else:
        print("\nWrong Input!!! Please try again.")


print('\nBye Bye!!! \n')
