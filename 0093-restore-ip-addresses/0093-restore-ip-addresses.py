class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        s = "25525511135"
        
        2.5.5.255, 2.5.525.5, 
        
        2.5.5.2, 2.5.5.25, 2.5.5.255, 2.5.52.551
        
        "255.255.11.135"
        
        
        
        checking the given digit is less than or = 12
        """
        
        res = []
        
        def is_valid(digit: str) -> bool:
            
            if not (0 <= int(digit) <= 255):
                return False
            
            if len(digit) > 1 and digit[0] == "0":
                return False
            
            return True
        
        def backtrack(idx, path):            
            if idx == len(s) and len(path) == 4:
                res.append(".".join(path))
                return
            
            if len(path) == 4 and idx < len(s):
                return
            
            digit = ""
            for i in range(idx, len(s)):
                digit += s[i]
                
                if not is_valid(digit):
                    continue
                path.append(digit)
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(0, [])
        return res
            