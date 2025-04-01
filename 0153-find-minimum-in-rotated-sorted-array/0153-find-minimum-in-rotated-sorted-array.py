class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = float("inf")

        if len(nums) == 1:
            return nums[0]

        while l <= r:
            mid = (l + r) // 2

            res = min(res, nums[mid])

            if nums[l] > nums[mid]:
                r = mid - 1
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res
