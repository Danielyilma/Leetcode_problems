class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}

        for i in range(len(nums)):
            reminder = target - nums[i]

            if reminder in rem:
                return [rem[reminder], i]
            rem[nums[i]] = i
        
        return []