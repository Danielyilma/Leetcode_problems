class Solution:
    def hIndex(self, citations: List[int]) -> int:
        leng = len(citations)
        res = 0

        low = 0
        high = len(citations) - 1


        while low <= high:
            mid = (low + high) // 2

            mins = min(citations[mid], leng - mid)
            res = max(mins, res)

            if citations[mid] >= leng - mid:
                high = mid - 1
            else:
                low = mid + 1

        return res
