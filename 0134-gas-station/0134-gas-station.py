class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = []
        suffix = [0]

        for i in range(len(gas)):
            total.append(gas[i] - cost[i])
        
        for i, val in enumerate(total[::-1]):
            suffix.append(suffix[i] + val)
        suffix.reverse()

        if suffix[0] < 0:
            return -1

        res = 0

        for i in range(len(suffix)):
            if suffix[res] < suffix[i]:
                res = i
        return res