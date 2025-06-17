class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        res = 0
        nums = []

        for i in range(len(nums1)):
            nums.append(nums1[i] - nums2[i])
        

        def merge(arr1, arr2):
            nonlocal res
            l = 0
            r = 0
            merged = []
            

            while l < len(arr1) and r < len(arr2):
                if arr1[l] <= arr2[r] + diff:
                    res += len(arr2) - r
                    l += 1
                else:
                    r += 1

            l = 0
            r = 0

            while l < len(arr1) or r < len(arr2):
                if r >= len(arr2) or (l < len(arr1) and arr1[l] <= arr2[r]):
                    merged.append(arr1[l])
                    l += 1
                else:
                    merged.append(arr2[r])
                    r += 1

            return merged
                
        
        def merge_sort(start, end, nums1):

            if start >= end:
                return [nums[end]]
            
            mid = (start + end) // 2
        
            left = merge_sort(start, mid, nums)
            right = merge_sort(mid+1, end, nums)

            return merge(left, right)
        
        s = merge_sort(0, len(nums) - 1, nums)

        return res