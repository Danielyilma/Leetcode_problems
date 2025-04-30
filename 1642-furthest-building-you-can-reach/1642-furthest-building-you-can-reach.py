class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        res = 0

        for i in range(1, len(heights)):
            
            if heights[i] - heights[i-1] > 0:
                heappush(heap, heights[i] - heights[i-1])

            if len(heap) == ladders + 1:
                num = heappop(heap)
                if num > bricks:
                    break
                bricks -= num
            res = i
                
        return res