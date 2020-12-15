ROW_LENGTH = 4
COL_LENGTH = 10
COLORS = 6

import pygame
import play

# Color codes for consistent use
white = (255, 255, 255)
red = (200, 0, 0)
dark_green = (0, 111, 2)
blue = (0, 0, 200)
black = (0, 0, 0)
yellow = (255, 255, 0)
gray = (30, 30, 30)
grey = (50, 50, 50)
grae = (100, 100, 100)


# Distances for consistency
WIDTH = 600
HEIGHT = 800
MARGIN = 25
PEG_SIZE = 10
PIECE_SIZE = 50

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Declare a font
FONT = pygame.font.Font("freesansbold.ttf", 50)


"""
Main / UI Definitions
"""

def start_game(bo):
    # Variable declaration
    clock = pygame.time.Clock()  # Clock timer for looping purposes
    color = 0                    # Set current color to 0 indicating no color currently selected
    turn_number = 1              # Start the turn number at 1
    s_x = -100                   # Start the x coordinate of the color indicator at -100 to be off screen
    s_y = -100                   # Start the y coordinate of the color indicator at -100 to be off screen
    offset = 0                   # Start the row coordinate offset at 0 because no offset currently needed
    game_statement = ""          # Set the string to display when a win / loss has occurred to empty
    leave = False                # Set the has exited the game boolean to False

    # The color picker buttons
    white_button = pygame.Rect(25, 10, PIECE_SIZE, PIECE_SIZE)
    blue_button = pygame.Rect(125, 10, PIECE_SIZE, PIECE_SIZE)
    black_button = pygame.Rect(225, 10, PIECE_SIZE, PIECE_SIZE)
    yellow_button = pygame.Rect(325, 10, PIECE_SIZE, PIECE_SIZE)
    red_button = pygame.Rect(425, 10, PIECE_SIZE, PIECE_SIZE)
    green_button = pygame.Rect(525, 10, PIECE_SIZE, PIECE_SIZE)

    # The current row buttons
    first_button = pygame.Rect(75, 80, PIECE_SIZE, PIECE_SIZE)
    second_button = pygame.Rect(175, 80, PIECE_SIZE, PIECE_SIZE)
    third_button = pygame.Rect(275, 80, PIECE_SIZE, PIECE_SIZE)
    fourth_button = pygame.Rect(375, 80, PIECE_SIZE, PIECE_SIZE)
    submit_button = pygame.Rect(12, 80, PIECE_SIZE, PIECE_SIZE)


    guess_array = []
    score_array = []

    # Create the array of rows
    for i in range(0, COL_LENGTH):
        guess_array.append(play.Attempt([0, 0, 0, 0]))
        score_array.append([0, 0, 0])

    # Print the answer to the console for testing, currently commented out
    # print(bo.answer)

    done = False
    # Main while loop for the game
    while not done:
        # If a pygame event occurs
        for event in pygame.event.get():
            # If it is to quit
            if event.type == pygame.QUIT:
                # End this loop and the extra loop
                done = True
                leave = True
            # If a mouse button has been clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # If on the white button
                if white_button.collidepoint(event.pos):
                    # Set the color to white
                    color = 1
                    # Update the color indicator coordinates
                    s_x = 45
                    s_y = 30

                # If on the blue button
                elif blue_button.collidepoint(event.pos):
                    # Set the color to blue
                    color = 2
                    # Update the color indicator coordinates
                    s_x = 145
                    s_y = 30

                # If on the black button
                elif black_button.collidepoint(event.pos):
                    # Set the color to black
                    color = 3
                    # Update the color indicator coordinates
                    s_x = 245
                    s_y = 30

                # If on the yellow button
                elif yellow_button.collidepoint(event.pos):
                    # Set the color to yellow
                    color = 4
                    # Update the color indicator coordinates
                    s_x = 345
                    s_y = 30

                # If on the red button
                elif red_button.collidepoint(event.pos):
                    # Set the color to red
                    color = 5
                    # Update the color indicator coordinates
                    s_x = 445
                    s_y = 30

                # If on the green button
                elif green_button.collidepoint(event.pos):
                    # Set the color to green
                    color = 6
                    # Update the color indicator coordinates
                    s_x = 545
                    s_y = 30

                # If on the first row button
                elif first_button.collidepoint(event.pos):
                    # Set that row piece to the current color
                    guess_array[turn_number - 1].row[0] = color

                # If on the second row button
                elif second_button.collidepoint(event.pos):
                    # Set that row piece to the current color
                    guess_array[turn_number - 1].row[1] = color

                # If on the third row button
                elif third_button.collidepoint(event.pos):
                    # Set that row piece to the current color
                    guess_array[turn_number - 1].row[2] = color

                # If on the fourth row button
                elif fourth_button.collidepoint(event.pos):
                    # Set that row piece to the current color
                    guess_array[turn_number - 1].row[3] = color

                # If on the submit row button
                elif submit_button.collidepoint(event.pos):
                    # Calculate the red and the white for this guess
                    guess_array[turn_number - 1].calculate_red_and_white(guess_array[turn_number - 1].row, bo.answer)
                    score_array[turn_number - 1][0] = guess_array[turn_number - 1].red
                    score_array[turn_number - 1][1] = guess_array[turn_number - 1].white
                    score_array[turn_number - 1][2] = score_array[turn_number - 1][0] + score_array[turn_number - 1][1]

                    # If all match
                    if score_array[turn_number - 1][0] == 4:
                        # Declare the user a winner!
                        done = True
                        game_statement = "You win!"

                    # If not all match
                    else:
                        # Increment the turn and offset
                        turn_number += 1

                        # If guess 10 has occurred
                        if turn_number == 11:
                            # Declare the user a loser
                            done = True
                            game_statement = "You lose!"

                        # If the user has more turns
                        else:
                            # Increment the coordinate offset by 60
                            offset += 60
                            # Increment the buttons by one row
                            first_button = pygame.Rect(75, 80 + offset, PIECE_SIZE, PIECE_SIZE)
                            second_button = pygame.Rect(175, 80 + offset, PIECE_SIZE, PIECE_SIZE)
                            third_button = pygame.Rect(275, 80 + offset, PIECE_SIZE, PIECE_SIZE)
                            fourth_button = pygame.Rect(375, 80 + offset, PIECE_SIZE, PIECE_SIZE)

        # Pygame Draw commands to display the game to the screen
        screen.fill(grey)
        select_display = pygame.Rect(s_x, s_y, PEG_SIZE, PEG_SIZE)
        submit_button = pygame.Rect(12, 80 + offset, PIECE_SIZE, PIECE_SIZE)
        pygame.draw.rect(screen, blue, blue_button)
        pygame.draw.rect(screen, black, black_button)
        pygame.draw.rect(screen, dark_green, green_button)
        pygame.draw.rect(screen, red, red_button)
        pygame.draw.rect(screen, yellow, yellow_button)
        pygame.draw.rect(screen, white, white_button)
        pygame.draw.rect(screen, grae, submit_button)
        pygame.draw.rect(screen, grey, select_display)

        # Pygame draw the win / loss condition to the screen, will be blank if no win / loss has occurred
        text_surf = FONT.render(game_statement, True, black)
        text_rect = text_surf.get_rect(center=(WIDTH / 2, 710))
        screen.blit(text_surf, text_rect)

        # Coordinates for drawing the rows of guesses, empty or otherwise
        p_x = 75
        p_y = 80

        # For every row of filled in or currently being filled in guesses
        for i in range(1, turn_number + 1):
            # For every piece in that row & the peg box
            for j in range(0, ROW_LENGTH + 1):
                # Declare the coordinates of that box
                placement = pygame.Rect(p_x, p_y, PIECE_SIZE, PIECE_SIZE)

                # If the box is a peg box, and is not out of bounds
                if j == ROW_LENGTH and i < COL_LENGTH + 1:
                    # Draw the peg box
                    pygame.draw.rect(screen, grae, placement)

                # If the box is not a peg box and is in bounds
                elif i < COL_LENGTH + 1:
                    # Draw the guess box
                    pygame.draw.rect(screen, get_color(guess_array[i - 1].row[j]), placement)
                # Increment the x coordinate for the row
                p_x += 100

            # For a new row, set the x coordinate to the start, and increment the y
            p_y += 60
            p_x = 75

        # If there are more turns
        if turn_number != 11:
            # For every remaining row
            for i in range(turn_number + 1, COL_LENGTH + 1):
                # For every piece in that row
                for j in range(0, ROW_LENGTH + 1):
                    # Draw each box of the row
                    placement = pygame.Rect(p_x, p_y, PIECE_SIZE, PIECE_SIZE)
                    pygame.draw.rect(screen, grae, placement)
                    # Increment the x coordinate for the row
                    p_x += 100

                # For a new row, set the x coordinate to the start, and increment the y
                p_y += 60
                p_x = 75

        # For every row of the peg array
        for i in range(0, len(score_array)):
            # Declare the peg coordinate variables
            peg_x = 0
            peg_y = i * 60 + 80
            # Set the red score to a temporary variable
            r = score_array[i][0]
            # If the peg count is not 0
            if score_array[i][2] > 0:
                # For every peg
                for j in range(0, score_array[i][2]):
                    # Create the peg
                    peg_display = pygame.Rect(485 + peg_x, 10 + peg_y, PEG_SIZE, PEG_SIZE)
                    if r > 0:
                        # If red display it in red
                        pygame.draw.rect(screen, red, peg_display)
                        r -= 1
                    else:
                        # If white display it in white
                        pygame.draw.rect(screen, white, peg_display)

                    # Adjust the coordinates for the next peg
                    peg_x += 20
                    if j == 1:
                        peg_y += 20
                        peg_x -= 40

        # Display the screen update
        pygame.display.update()

        # Update the loop based the clock
        clock.tick(30)

    # If the game is over, print the answer at the bottom
    a_x = 75
    a_y = 740
    for i in range(0, ROW_LENGTH):
        answer_placement = pygame.Rect(a_x, a_y, PIECE_SIZE, PIECE_SIZE)
        pygame.draw.rect(screen, get_color(bo.answer[i]), answer_placement)
        a_x += 100

    # Update the screen to display the answer
    pygame.display.update()

    # If the user has won / lost and has not hit the quit button
    while done and not leave:
        # Wait until they hit the quit button to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False

    # Quit the game
    pygame.quit()

# Gets the color from the number representing the color in a play object or otherwise
def get_color(c):
    if c == 1:
        return white
    elif c == 2:
        return blue
    elif c == 3:
        return black
    elif c == 4:
        return yellow
    elif c == 5:
        return red
    elif c == 6:
        return dark_green
    else:
        return grae