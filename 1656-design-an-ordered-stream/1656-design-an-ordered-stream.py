class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * (n + 1)
        self.stream_at = 1
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        if idKey != self.stream_at:
            return []
        
        res = []

        for i in range(idKey, len(self.stream)):
            if not self.stream[i]:
                break
            res.append(self.stream[i])
            self.stream_at += 1

        
        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)