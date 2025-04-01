class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = {c: i for i, c in enumerate(s)}
        l = start = 0
        res = []

        for i, c in enumerate(s):
            l = max(l, last[c])

            if l == i:
                res.append(i - start + 1)
                start = i + 1
                l += 1
        return res