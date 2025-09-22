class Solution:
    def climbStairs(self, n: int) -> int:
        store = {}

        def rec(cur):
                
            if cur == n:
                return 1
            
            if cur > n:
                return 0

            if cur not in store:
                store[cur] = rec(cur + 1) + rec(cur + 2)

            return store[cur]
        
        return rec(0)