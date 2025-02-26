from colorama import Fore
from utils.utils import print_color

class GuessNumber:
    def __init__(self, range_top):
        self.range_top = range_top
        self.range_bottom = 0
        self.history = []

    def guess(self):
        guess = (self.range_bottom + self.range_top) // 2
        self.history.append(guess)
        return guess

    def raise_cheating_exception(self):
        raise Exception('No more numbers to guess in range. You are cheating!')

    def handle_win_feedback(self, feedback):
        if feedback == 'n' and self.range_bottom == self.range_top:
            self.raise_cheating_exception()
        return feedback == 'y'

    def handle_feedback(self, feedback):
        last_guess = self.history[-1]
        if feedback == 'y':
            if last_guess == self.range_bottom:
                self.raise_cheating_exception()
            self.range_top = last_guess - 1
        else:
            if last_guess == self.range_top:
                self.raise_cheating_exception()
            self.range_bottom = last_guess + 1

class ManageGuessNumber:
    def __init__(self):
        range_top = int(input("Enter the range top: "))
        self.game = GuessNumber(range_top)

    def print_status(self):
        print_color(f"History: {self.game.history}", color=Fore.CYAN)
        print_color(f"Guesses so far: {len(self.game.history)} | range: ({self.game.range_bottom}, {self.game.range_top})", color=Fore.CYAN)

    def playGame(self):
        has_won = False
        while not has_won:
            self.print_status()
            guess = self.game.guess()

            try:
                feedback = str(input(f"Is {guess} correct? (y/n): "))
                has_won = self.game.handle_win_feedback(feedback)
                if has_won:
                    print_color('Winner!', color=Fore.GREEN)
                    break

                feedback = str(input(f"Is {guess} too high? (y/n): "))
                self.game.handle_feedback(feedback)
            except ValueError:
                print_color('Invalid input', color=Fore.RED)
            except Exception as e:
                print_color(e, color=Fore.RED)
                break
        print_color(f'The number was {self.game.history[-1]}', color=Fore.CYAN)

manageGuessNumber = ManageGuessNumber()
manageGuessNumber.playGame()
