class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums)
        top = sorted(res.items(), key=lambda x: x[1], reverse=True)
        return list(map(lambda x: x[0], top[:k]))
