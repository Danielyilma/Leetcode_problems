class Solution:
    def decodeString(self, s: str) -> str:
        
        num = ""
        res = []
        i = 0
        temp = ""

        while i < len(s):
            if s[i].isnumeric():
                num += s[i]

            elif s[i] == "[":
                if temp:
                    res.append(temp)
                temp = ""
                count = 0
                j = i + 1
                while j < len(s) and (s[j] != "]" or count):
                    if s[j] == "[":
                        count += 1
                    
                    if s[j] == "]":
                        count -= 1
                    temp += s[j]
                    j += 1
                i = j

                if not num:
                    num = "1"
                res.append(int(num) * self.decodeString(temp))
                num = ""
                temp = ""
            else:
                temp += s[i]
            i += 1
        
        if temp:
            res.append(temp)
        
        return "".join(res)
