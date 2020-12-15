import board
import pygame
import ui

"""
Game Runners
"""

# Start pygame
pygame.init()
pygame.display.set_caption("Mastermind")

# Create a board
b = board.Board()
# Create an answer
b.create_answer()

# Menu Startup
ui.start_game(b)

# End Pygame
pygame.quit()

