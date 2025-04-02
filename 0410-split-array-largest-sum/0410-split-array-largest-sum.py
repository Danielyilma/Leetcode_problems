class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def validate(nums, ind, k):
            split = 0
            sums = 0

            for i in range(len(nums)):
                sums += nums[i]
                if sums > ind:
                    split += 1
                    sums = nums[i]
            
            return split >= k

        l = max(nums)
        h = sum(nums)

        while l <= h:
            mid = (l + h) // 2

            if validate(nums, mid, k):
                l = mid + 1
            else:
                h = mid - 1

        return h + 1

'''
{
    
}
'''