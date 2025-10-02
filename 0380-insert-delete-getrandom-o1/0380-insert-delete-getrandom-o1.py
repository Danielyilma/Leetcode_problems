class RandomizedSet:

    def __init__(self):
        self.data = {}
        self.arr_data = []
        self.capacity = 0

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        
        if self.capacity < len(self.arr_data):
            self.arr_data[self.capacity] = val
            self.data[val] = self.capacity
        else:
            self.arr_data.append(val)
            self.data[val] = len(self.arr_data) - 1

        self.capacity += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        
        idx = self.data[val]
        last_idx = self.capacity - 1
        self.arr_data[idx] = self.arr_data[last_idx]
        self.data[self.arr_data[idx]] = idx
        self.capacity -= 1
        del self.data[val]
        return True

    def getRandom(self) -> int:
        random_idx = random.randint(0, self.capacity -1)
        return self.arr_data[random_idx] 
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()