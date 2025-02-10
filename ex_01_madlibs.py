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

AUTO = False

class Madlibs:
  def __init__(self, number):
    self.number = number
    self.list = ['verbs', 'adjectives', 'nouns']
    self.verbs = []
    self.adjectives = []
    self.nouns = []

  def get_inputs(self, cat):
    current_list = getattr(self, cat, None)
    # first val
    new_value = STATIC_LIST[cat][0] if AUTO else input(f"Enter the first {cat}: ")
    current_list.append(new_value)

    # all following
    for index in range(1,self.number):
      new_value = STATIC_LIST[cat][index] if AUTO else input(f"Enter a {index} {cat}: ")
      insert_index = 0 if len(current_list) == 1 else random.randrange(0,len(current_list)-1)

      current_list.append(current_list[insert_index])
      current_list[insert_index] = new_value

  def get_all_inputs(self):
    for cat in ['verbs', 'adjectives', 'nouns']:
      self.get_inputs(cat)

  def generate_lib(self):
    response = []
    for index in range(self.number):
      response.append(f"One {self.nouns[index]} {self.verbs[index]} quite {self.adjectives[index]}")
    return response

number = 4 if AUTO else int(input("enter number of sentences: "))
m = Madlibs(number)
m.get_all_inputs()
result = m.generate_lib()
print(result)
