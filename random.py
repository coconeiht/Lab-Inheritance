import random

class RandomList(list):
    def get_random_element(self):
        if len(self) == 0:
            raise IndexError("Cannot get an element from an empty list")
        random_index = random.randint(0, len(self) - 1)
        return self.pop(random_index)