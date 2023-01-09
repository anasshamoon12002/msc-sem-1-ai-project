
from Players import Players

def test_multiplayer():
    play = Players()
    play.multiplayer(0)

# 0 is for human first 1 is for computer first
def test_computer(turn):
    play = Players()
    play.random_computer(turn)

# test_multiplayer()

# test_computer(0)

test_computer(1)