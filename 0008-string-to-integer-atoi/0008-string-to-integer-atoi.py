class Solution:
    def myAtoi(self, s: str) -> int:
        num_map = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0,
        }
        s = s.strip()

        if not s:
            return 0

        isneg = s[0] == "-"

        if isneg or s[0] == "+":
            st = s[1:]
        else:
            st = s
        res = 0

        for i in range(len(st)):
            if st[i] not in num_map:
                break
            res = res * 10 + num_map[st[i]]
        
        if isneg:
            res = (-1 * res)
        
        if res < -2 ** 31:
            res = -2 ** 31
        elif res >= 2 ** 31:
            res = (2 ** 31) - 1


        return res

