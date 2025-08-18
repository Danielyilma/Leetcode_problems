class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        leng = max(len(g), len(s))
        res = 0

        j = 0
        for i in range(leng):
            if j >= len(g) or i >= len(s):
                break
    
            if g[j] <= s[i]:
                res += 1
                j += 1

        return res