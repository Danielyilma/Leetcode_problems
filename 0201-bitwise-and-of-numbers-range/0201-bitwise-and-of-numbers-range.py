class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0
        leng = right - left
        k = 0

        while k < 32:
            if leng <= 2 ** k:
                val = ((left & (1 << k)) and (right & (1 << k)))

                if not (res & (1 << k)) and val:
                    res = res ^ (1 << k)
            k += 1
        return res

                