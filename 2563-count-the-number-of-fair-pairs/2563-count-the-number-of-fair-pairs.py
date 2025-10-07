class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def bound_search(start, target, compare):
            low = start
            high = len(nums)

            while low < high:
                mid = (low + high) // 2

                if compare(nums[mid], target):
                    high = mid
                else:
                    low = mid + 1
            
            return low
        
        lower_bound = lambda elem, target: elem >= target  
        upper_bound = lambda elem, target: elem > target 

        """
            0 + x <= upper
            0 + x >= lower

            upper - elem >= x
            lower - elem >= x
        """

        res = 0
        for i in range(len(nums) - 1):
            local_upper = upper - nums[i]
            local_lower = lower - nums[i]

            lower_idx = bound_search(i + 1, local_lower, lower_bound)
            upper_idx = bound_search(i + 1, local_upper + 1, lower_bound)
            res += upper_idx - lower_idx  

        return res


