class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reminder = {}

        for i in range(len(nums)):
            if nums[i] in reminder:
                return [reminder[nums[i]], i]
            reminder[target - nums[i]] = i
        
        return [0, 0]