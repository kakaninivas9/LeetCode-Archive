import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False

        self.arr.append(val)
        self.pos[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False

        index = self.pos[val]
        last = self.arr[-1]

        self.arr[index] = last
        self.pos[last] = index

        self.arr.pop()
        del self.pos[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# print(obj.insert(1))      # True
# print(obj.remove(2))      # False
# print(obj.insert(2))      # True
# print(obj.getRandom())    # 1 or 2
# print(obj.remove(1))      # True
# print(obj.insert(2))      # False
# print(obj.getRandom())    # 2