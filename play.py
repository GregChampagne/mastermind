ROW_LENGTH = 4

class Attempt:

    # A row constructor for a given guess
    def __init__(self, guess, answer):
        self.row = guess
        self.red = 0
        self.white = 0
        self.calculate_red_and_white(guess, answer)

    def calculate_red_and_white(self, guess, answer):
        # Copy guess and answer to temporary arrays
        g = guess.copy()
        a = answer.copy()

        # Find all of the red spots
        for i in range(0, ROW_LENGTH):
            if int(g[i]) == int(a[i]):
                self.red += 1
                # Denote found spots as found
                g[i] = -1
                a[i] = -2

        # Find all of the white spots
        for i in range(0, ROW_LENGTH):
            if g[i] != -1:
                for j in range(0, ROW_LENGTH):
                    if int(g[i]) == int(a[j]):
                        self.white += 1
                        # Denote found spots as found
                        g[i] = -1
                        a[j] = -2

    # Print out a given guess
    def printout(self):
        printout = ""
        for i in range(0, ROW_LENGTH):
            printout += str(self.row[i]) + " "

        printout += "- R:" + str(self.red) + " W:" + str(self.white)

        print(printout)
