"""
  input a number of variables
  input each variable for each category
  do the madlibs
"""

import random

STATIC_LIST = {
  'verbs': ['flew', 'drew', 'fainted', 'drove'],
  'adjectives': ['pretty', 'tired', 'joyful', 'fast'],
  'nouns': ['house', 'car', 'banana', 'phone'],
}

AUTO = True

class Madlibs:
  def __init__(self, number):
    self.number = number
    self.data = {
      "verbs": [],
      "adjectives": [],
      "nouns": [],
    }

  def append_to_data(self, cat, data):
    self.data[cat].append(data)

  def generate_lib(self):
    response = []

    for index in range(self.number):
      for cat in self.data:
        random_index = random.randrange(index, self.number)
        temp = self.data[cat][index]
        self.data[cat][index] = self.data[cat][random_index]
        self.data[cat][random_index] = temp
      response.append(f"One {self.data['nouns'][index]} {self.data['verbs'][index]} quite {self.data['adjectives'][index]}")
    return response

class GetUserInputs:
  def __init__(self):
    number = 4 if AUTO else int(input("enter number of sentences: "))
    self.madlibs = Madlibs(number)

  def get_inputs(self):
    for cat in self.madlibs.data:
      for index in range(self.madlibs.number):
        current = STATIC_LIST[cat][index] if AUTO else input(f"Enter a {index+1} {cat}: ")
        self.madlibs.append_to_data(cat,current)

  def print_madlib(self):
    response = self.madlibs.generate_lib()
    print(response)

g = GetUserInputs()
g.get_inputs()
g.print_madlib()
g.print_madlib()
g.print_madlib()