class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        store = {}

        def rec(idx, prev):
            if idx >= len(nums):
                return 0

            take = 0
            not_take = 0

            if prev < nums[idx] and idx not in store:
                take = rec(idx + 1, nums[idx]) + 1
                store[idx] = take
            elif prev < nums[idx]:
                take = store[idx]
                store[idx] = take
    
            not_take = rec(idx + 1, prev)
            
            return max(take, not_take)
        
        return rec(0, float("-inf"))