class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [0]
        res = []

        for i in range(len(arr)):
            pref.append(pref[i] ^ arr[i])
        
        for x, y in queries:
            res.append(pref[y + 1] ^ pref[x])
        
        return res
