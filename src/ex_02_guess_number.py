import random
from colorama import Fore
from utils.utils import print_color

class GuessResult:
    def __init__(self, result, too_high):
        self.result = result
        self.too_high = too_high

class GuessNumber:
    def __init__(self, number):
        self.number = number
        self.history = []

    def guess(self, guess):
        self.history.append(guess)
        return GuessResult(guess == self.number, guess > self.number)

class ManageGuessNumber:
    def __init__(self):
        self.maxAttempts = 5
        self.game = GuessNumber(random.randint(1, 100))

    def print_status(self):
        attempts_left = self.maxAttempts - len(self.game.history)
        print_color(f"History: {self.game.history}", color=Fore.CYAN)
        print_color(f"Guesses left: {attempts_left}", color=Fore.CYAN)

    def playGame(self):
        while len(self.game.history) < self.maxAttempts:
            self.print_status()
            try:
                guess = int(input("Enter a guess: "))
                result = self.game.guess(guess)
                if result.result:
                    print_color('Winner!', color=Fore.GREEN)
                    break
                print_color('Too High' if result.too_high else 'Too Low', color=Fore.RED)
            except ValueError:
                print_color('Invalid input', color=Fore.RED)
        else:
            print_color('Game Over', color=Fore.RED)
        print_color(f'The number was {self.game.number}', color=Fore.CYAN)

manageGuessNumber = ManageGuessNumber()
manageGuessNumber.playGame()