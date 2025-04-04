class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        cost = 0
        count_r = [0] * len(instructions)
        count_l = [0] * len(instructions)



        def merge(left, right):
            nonlocal cost
            l = 0
            r = 0
            merged = []
            count = defaultdict(int)


            while l < len(left) or r < len(right):
                if r >= len(right) or (l < len(left) and instructions[left[l]] <= instructions[right[r]]):
                    count[instructions[left[l]]] += 1
                    merged.append(left[l])
                    l += 1
                elif r < len(right):
                    count_r[right[r]] += len(left) - l 
                    count_l[right[r]] += (l - count[instructions[right[r]]])

                    merged.append(right[r])
                    r += 1

            return merged

        
        def merge_sort(left_ind, right_ind):

            if left_ind >= right_ind:
                return [left_ind]
            
            mid = (left_ind + right_ind) // 2

            left = merge_sort(left_ind, mid)
            right = merge_sort(mid + 1, right_ind)
        
            return merge(left, right)

        merge_sort(0, len(instructions) - 1)

        for left, right in zip(count_l, count_r):
            cost += min(left, right) % (10**9 + 7)
            cost %= (10**9 + 7)

        return cost
            