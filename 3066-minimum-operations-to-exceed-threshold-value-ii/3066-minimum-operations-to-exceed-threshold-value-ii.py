class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        no_gre = 0
        res = 0

        for num in nums:
            heappush(heap, num)
            if num >= k:
                no_gre += 1
            
        if len(heap) == no_gre:
            return res
        
        while len(heap) >= 2:
            num1 = heappop(heap)
            num2 = heappop(heap)

            if num1 >= k:
                no_gre -= 1
            
            if num2 >= k:
                no_gre -= 1

            num = (min(num1, num2) * 2 + max(num1, num2))
            heappush(heap, num)
            if num >= k:
                no_gre += 1
            
            res += 1
            if len(heap) == no_gre:
                break
        

        return res



