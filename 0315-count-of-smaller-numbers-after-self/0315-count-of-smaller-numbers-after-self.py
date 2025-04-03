class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)

        def merge(left, right):
            nonlocal count

            l, r = 0, 0
            merged = []

            while l < len(left) or r < len(right):
                if r >= len(right) or l < len(left) and nums[left[l]] <= nums[right[r]]:
                    count[left[l]] += max(len(merged) - l, 0)
                    merged.append(left[l])
                    l += 1
                elif r < len(right):
                    count[right[r]] += max(len(merged) - (len(left) + r), 0)
                    merged.append(right[r])
                    r += 1

            return merged



        def merge_sort(start, end, nums):
            if start == end:
                return [start]

            mid = (start + end) // 2

            left = merge_sort(start, mid, nums)
            right = merge_sort(mid + 1, end, nums)

            return merge(left, right)

        merge_sort(0, len(nums) - 1, nums)

        return count