ROW_LENGTH = 4

import play

class Mastermind:
    # Mastermind Game Constructor
    def __init__(self, b):
        self.board = b

    # Main playable function
    def play_game(self):
        # While the player is still playing
        while not self.board.lose and not self.board.win:
            # Get their guess
            first = input("First number: ")
            second = input("Second number: ")
            third = input("Third number: ")
            fourth = input("Fourth number: ")

            # Input their guess to the board
            x = play.Attempt([first, second, third, fourth], self.board.answer)
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

    # Print the answer in the case of a win or a loss
    def print_answer(self):
        printout = ""
        for i in range(0, ROW_LENGTH):
            printout += str(self.board.answer[i]) + " "

        print(printout)