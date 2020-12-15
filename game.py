ROW_LENGTH = 4

import play

class Mastermind:
    # Mastermind Game Constructor
    def __init__(self, b, choice):
        print("I'VE BEEN CLICKED")
        self.board = b
        if choice:
            self.play_ai()
        else:
            self.two_player()

    # Main playable function
    def play_ai(self):
        go = True
        while go:
            # Reset the answer to the game
            self.board.create_answer()
            # While the player is still playing
            while not self.board.lose and not self.board.win:
                # Get their guess
                first = input("First number: ")
                second = input("Second number: ")
                third = input("Third number: ")
                fourth = input("Fourth number: ")

                # Input their guess to the board
                x = play.Attempt([first, second, third, fourth])
                self.board.input_play(x)

                # DEBUGGING STATEMENT THAT GIVES AWAY ANSWER
                # self.print_answer()

            # Check for a win or loss
            if self.board.win:
                self.print_answer()
                print("Congrats you won!")
            else:
                self.print_answer()
                print("uh oh, dumbo!")

            x = input("Would you like to play again? Enter 1 for yes")
            if x != 1:
                go = False

    def two_player(self):
        print("soon")


    # Print the answer in the case of a win or a loss
    def print_answer(self):
        printout = ""
        for i in range(0, ROW_LENGTH):
            printout += str(self.board.answer[i]) + " "

        print(printout)