class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        store = {}

        def recur(idx):
            if idx >= len(cost):
                return 0
            
            if idx in store:
                return store[idx]
            
            one = recur(idx + 1) + cost[idx]
            two = recur(idx + 2) + cost[idx]

            store[idx] = min(one, two)
            return store[idx]

        return min(recur(0), recur(1))