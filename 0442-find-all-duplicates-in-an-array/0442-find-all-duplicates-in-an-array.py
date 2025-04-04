class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup = set()
        mis = -1
        duplicate = set()
        i = 0

        while i < len(nums):
            if i != nums[i] - 1 and nums[i] not in dup:
                dup.add(nums[i])
                ind = nums[i]
                nums[ind - 1], nums[i] = nums[i], nums[ind - 1]
            elif i != nums[i] - 1 and nums[i] in dup:
                duplicate.add(nums[i])
                i += 1
            else:
                dup.add(nums[i])
                i += 1
        
        return list(duplicate)