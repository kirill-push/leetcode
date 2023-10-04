import random


class RandomizedSet:
    def __init__(self):
        self.dict = dict()
        self.elements = []

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.elements)
            self.elements.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        else:
            i = self.dict[val]
            last_elem = self.elements[-1]

            self.elements[i] = last_elem
            self.dict[last_elem] = i

            self.elements.pop()
            self.dict.pop(val)

            return True

    def getRandom(self) -> int:
        return random.choice(self.elements)
