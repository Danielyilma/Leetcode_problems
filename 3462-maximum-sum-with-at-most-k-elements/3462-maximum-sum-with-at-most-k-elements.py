class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        res = 0

        for i, g in enumerate(grid):
            heap.extend(sorted(g, reverse=True)[:limits[i]])
        
        heap = list(map(lambda x: -x, heap))
        heapify(heap)

        while k:
            res -= heappop(heap)
            k -= 1
        return res
        

        