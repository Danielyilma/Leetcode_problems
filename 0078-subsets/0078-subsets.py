class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        n = (1 << len(nums))

        for i in range(n):
            num = i
            k = 0
            temp = []

            while k < len(nums):
                if num & (1 << k):
                    temp.append(nums[k])
                k += 1
            
            res.append(temp)
        
        return res