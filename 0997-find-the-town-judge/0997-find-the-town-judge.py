class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        town = [0] * n
        count = defaultdict(int)

        for a, b in trust:
            town[a - 1] = 1
            count[b - 1] += 1 
        
        for i in range(len(town)):
            if town[i] == 0 and count[i] == n - 1:
                return i + 1
        return -1