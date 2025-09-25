class Solution:
    store = {}
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        
        if n == 2:
            return 1
        
        if n not in self.store:
            self.store[n] = self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
        
        return self.store[n]