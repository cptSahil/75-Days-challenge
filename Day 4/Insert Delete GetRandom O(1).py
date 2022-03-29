class RandomizedSet:

    def __init__(self):
        self.data={}

    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.data[val]=1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.data:
            self.data.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.data.keys()))