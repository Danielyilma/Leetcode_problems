class Solution:
    def rob(self, nums: List[int]) -> int:
        store = {}

        def rec(index, money):
            if index >= len(nums):
                return money

            if (index, money) not in store:
                steal = rec(index + 2, money + nums[index])
                not_steal = rec(index + 1, money)
                store[(index, money)] = max(steal, not_steal)

            return store[(index, money)]
        
        return rec(0, 0)

