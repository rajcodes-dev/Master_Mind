import random

class GameController:
    """Run the game."""
    COLORS = ['R','G','B','V','W','O']
    random_COLORS = random.choices(COLORS, weights=None, cum_weights=None, k=4)
    guess_count = 0

    def __init__(self, ui):
        self.ui = ui

    def run(self):
        ui.greet()
        print(GameController.random_COLORS)
        while True:
            correct_position = 0
            wrong_position = 0
            guesses = ui.user()
            GameController.guess_count += 1
            empty = []

            for n in range(0,len(GameController.random_COLORS)):
                if guesses[n] in GameController.random_COLORS:
                    if GameController.random_COLORS[n] in guesses[n]:
                        correct_position += 1
                        empty.append(guesses[n])
                    elif guesses[n] not in empty:
                        wrong_position += 1

            ui.position(correct_position, wrong_position)

            if correct_position == 4:
                print("You Win!")
                break

            if GameController.guess_count == 10:
                print("Game Over! you can't be able to guess the number in 10 guesses.")
                break

class UserInterface:
    """Display the overall program."""

    def greet(self):
        print("Welcome to MasterMind!".center(50))
        print("Guess the word in 4 guesses. On 10 Tries".center(50))
        print(f"COLORS are based on colors which are: {GameController.COLORS}")

    def user(self):
        return input("Guesses!(Separated by spaces): ").upper().split()

    def position(self, correct_position, wrong_position):
        print(f"Correct Position: {correct_position}", end=' ')
        print(f"| Wrong Position: {wrong_position}\n")

if __name__ == '__main__':
    ui = UserInterface()
    game = GameController(ui)
    game.run()