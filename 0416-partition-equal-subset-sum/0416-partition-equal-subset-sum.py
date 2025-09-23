class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        store = {}
        half = sum(nums) / 2

        if half != int(half):
            return False

        def partition(index, num):
            if num == 0:
                return True
            
            if num < 0 or index >= len(nums):
                return False

            key = (index + num) * (index + num + 1) // 2 + num
            if key not in store:
                add = partition(index + 1, num - nums[index])
                not_add = partition(index + 1, num)

                store[key] = add or not_add
            
            return store[key]

        return partition(0, half)