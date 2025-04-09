class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0] * n
        out_degree = [0] * n

        for a, b in edges:
            in_degree[b] += 1
            out_degree[a] += 1
        
        res = []

        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                res.append(i)
        
        if len(res) > 1:
            return -1
        return res[0]