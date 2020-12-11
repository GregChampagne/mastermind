ROW_LENGTH = 4
COLORS = 6

import board
import game
import random

# Create a random answer
arr = []
for i in range(0, ROW_LENGTH):
    arr.append(random.randint(1, COLORS))

# a = [2, 2, 3, 3]
a = arr

# Send the random answer into a new board
b = board.Board(a)

# Create a game using the board
g = game.Mastermind(b)

# Play a game
g.play_game()
