class RandomizedSet:

    def __init__(self):
        self.vals = set()

    def insert(self, val: int) -> bool:
        if val not in self.vals:
            self.vals.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.vals:
            return False
        else:
            self.vals.remove(val)
            return True

    def getRandom(self) -> int:
        return random.sample(self.vals, 1)[0]