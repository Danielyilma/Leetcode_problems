class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        store = {}

        def recur(idx, purchased):
            if idx >= len(prices):
                return 0

            if (idx, purchased) in store:
                return store[idx, purchased]
            
            passed = recur(idx + 1, purchased)
            profit = 0

            if purchased:
                profit = recur(idx + 1, not purchased) + prices[idx]
            else:
                profit = recur(idx + 1, not purchased) - prices[idx] - fee
            
            store[(idx, purchased)] = max(profit, passed)
            return store[idx, purchased]
        
        return recur(0, False)
            
