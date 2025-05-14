class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        count = 0
        k = 0
    
        while k < 32:
            if z & (1 << k):
                count += 1
            k += 1
        
        return count