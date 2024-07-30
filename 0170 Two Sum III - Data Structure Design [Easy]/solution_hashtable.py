from collections import defaultdict

class TwoSum:

    def __init__(self):
        self.TwoSum = []
        self.hashmap = defaultdict(int)

    def add(self, number: int) -> None:
        self.TwoSum.append(number)
        self.hashmap[number] += 1
        
    def find(self, value: int) -> bool:
        for num in self.TwoSum:
            if (value - num) in self.hashmap:
                #value - num == num: possibility of (a) pair(s) of identical number
                #but if self.hashmap[num] == 1: there is only one such number -> cannot form a pair of two identical numbers
                if value - num == num and self.hashmap[value - num] == 1:
                    continue
                #otherwise: pairs of different numbers
                return True
        
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)