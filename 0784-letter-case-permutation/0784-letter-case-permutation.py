class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        indexs = []
        res = []

        for i in range(len(s)):
            if s[i].isalpha():
                indexs.append(i)
        
        for i in range(2 ** len(indexs)):
            res.append(list(s))
            k = 0

            while k < len(indexs):
                if i & (1 << k):
                    res[-1][indexs[k]] = res[-1][indexs[k]].upper()
                else:
                    res[-1][indexs[k]] = res[-1][indexs[k]].lower()
                k += 1
            res[-1] = "".join(res[-1])

        return res