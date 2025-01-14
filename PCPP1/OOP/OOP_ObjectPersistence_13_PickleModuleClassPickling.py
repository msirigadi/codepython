"""
class definition and object pickling
"""

import pickle

class Cucumber:
    def __init__(self):
        self.size = 'small'

    def get_size(self):
        return self.size

cucu = Cucumber()

with open('cucumber.pck1', 'wb') as file_out:
    pickle.dump(cucu, file_out)