import random, traceback
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

STATIC_LIST = {
    "verbs": ["flew", "drew", "fainted", "drove"],
    "adjectives": ["pretty", "tired", "joyful", "fast"],
    "nouns": ["house", "car", "banana", "phone"],
}

AUTO = True

def print_color(message, **kwargs):
    color = kwargs.get('color', Fore.WHITE)
    bold = kwargs.get('bold', False)
    style = Style.BRIGHT if bold else Style.NORMAL
    print(f"{color}{style}{message}{Style.RESET_ALL}")

class Madlibs:
    def __init__(self, number):
        self.number = number
        self.data = {
            "nouns": [],
            "verbs": [],
            "adjectives": [],
        }

    def append_to_data(self, cat, data):
        self.data[cat].append(data)

    def generate_lib(self):
        print_color("::MadLibs.generate_lib::", bold=True)
        response = []
        last_index = self.number-1
        for index in range(last_index):
            for cat in self.data:
                random_index = random.randrange(index, self.number)
                temp = self.data[cat][index]
                self.data[cat][index] = self.data[cat][random_index]
                self.data[cat][random_index] = temp
            sentence = f"One {self.data['nouns'][index]} {self.data['verbs'][index]} quite {self.data['adjectives'][index]}"
            response.append(sentence)
        sentence = f"One {self.data['nouns'][last_index]} {self.data['verbs'][last_index]} quite {self.data['adjectives'][last_index]}"
        response.append(sentence)
        return response

class GetUserInputs:
    def __init__(self, auto, static_list):
        self.static_list = static_list
        self.auto = auto
        number = 4 if self.auto else int(input("enter number of sentences: "))
        self.madlibs = Madlibs(number)

    def get_inputs(self):
        print_color("::GetUserInputs.get_inputs::",bold=True)
        for cat in self.madlibs.data:
            for index in range(self.madlibs.number):
                current = (
                    self.static_list[cat][index]
                    if self.auto
                    else input(f"Enter a {index+1} {cat}: ")
                )
                self.madlibs.append_to_data(cat, current)

    def print_madlib(self):
        print_color("::GetUserInputs.print_madlib::",bold=True)
        response = self.madlibs.generate_lib()
        print_color(response, color=Fore.GREEN)

# g = GetUserInputs(AUTO, STATIC_LIST)
# g.get_inputs()
# g.print_madlib()
# g.print_madlib()
# g.print_madlib()
