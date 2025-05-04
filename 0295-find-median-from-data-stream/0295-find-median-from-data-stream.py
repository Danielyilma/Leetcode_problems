class MedianFinder:

    def __init__(self):
        self.inc_heap = []
        self.dec_heap = []
        self.cap = 0

    def addNum(self, num: int) -> None:
        self.cap += 1

        if not self.dec_heap or num >= self.dec_heap[0]:
            heappush(self.dec_heap, num)
            if len(self.dec_heap) > math.ceil(self.cap / 2):
                n = heappop(self.dec_heap)
                heappush(self.inc_heap, -1 * n)
        else:
            heappush(self.inc_heap, -1 * num)
            if len(self.inc_heap) > math.ceil(self.cap / 2):
                n = heappop(self.inc_heap)
                heappush(self.dec_heap, -1 * n)
      

    def findMedian(self) -> float:
        if len(self.inc_heap) == len(self.dec_heap):
            return (self.dec_heap[0] + -1 * self.inc_heap[0]) / 2
        elif len(self.inc_heap) > len(self.dec_heap):
            return -1 * self.inc_heap[0]
        else:
            return self.dec_heap[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()