import random
from enum import Enum
from colorama import Fore
from utils.utils import print_color

"""
- get user input for rock/paper/scissors
- computer generates random choice
- comparison on both and print result


future
- best 3 of 5
- UI for selecting with arrow keys


two ways to structure classes:
- one
    - class for game instance, unopinionated API
    - class for managing game
- two
    - class for game instance

(USER-COMPUTER) % 3 == 1 user wins

user    computer    (USER-COMPUTER)     modulo  result
---     ---         ---                 ---     ---
ROCK    PAPER       -1                  2       -1
ROCK    SCISS       -2                  1       1

PAPER   ROCK        1                   2       -1
PAPER   SCISS       -1                  2

SCISS   ROCK        2                   
SCISS   PAPER       1                   
"""

class Choices(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

class Game:
    def __init__(self):
        self.scores = { 'computer': 0, 'user': 0 }
        self.choices = list(Choices)

    def generate_computer_choice(self) -> Choices:
        return random.choice(self.choices)

    def compare_choices(self, user_choice: str) -> int:
        u_choice = Choices[user_choice]
        c_choice = self.generate_computer_choice()

        print_color(f"u_choice: {u_choice}", color=Fore.CYAN)
        print_color(f"c_choice: {c_choice}", color=Fore.CYAN)

        if c_choice == u_choice: return 0

        if (u_choice.value - c_choice.value) % 3 == 1: return 1
        else: return -1

    def update_scores(self, user_wins: bool) -> None:
        if user_wins:
            self.scores['user'] += 1
        else:
            self.scores['computer'] += 1

    def get_scores(self) -> dict:
        return self.scores


class ManageGame:
    def __init__(self):
        self.game = Game()

    def play_game(self):
        game_over = False
        while not game_over:
            try:
                user_input = str(input(f"Select (ROCK/PAPER/SCISSORS): "))
                result = self.game.compare_choices(user_input)

                if result == 0:
                    print_color('Draw!', color=Fore.CYAN)
                else:
                    self.game.update_scores(result == 1)
                    if result == -1:
                        print_color('Computer wins!', color=Fore.RED)
                    else:
                        print_color('You win!', color=Fore.GREEN)
                game_over = True
                print_color(f"Scores: {self.game.get_scores()}", color=Fore.CYAN)
            except KeyError:
                print_color('Invalid choice. Please choose ROCK, PAPER, or SCISSORS.', color=Fore.RED)
            except Exception as e:
                print_color(str(e), color=Fore.RED)

m = ManageGame()
m.play_game()
