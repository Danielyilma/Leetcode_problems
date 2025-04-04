class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dup = set()
        i = 0
        disapear = []

        while i < len(nums):
            if i != nums[i] - 1 and nums[i] not in dup:
                dup.add(nums[i])
                ind = nums[i]
                nums[ind - 1], nums[i] = nums[i], nums[ind - 1]
            elif i != nums[i] - 1 and nums[i] in dup:
                i += 1
            else:
                dup.add(nums[i])
                i += 1

        for i in range(len(nums)):
            if i != nums[i] - 1:
                disapear.append(i + 1)
        
        return disapear