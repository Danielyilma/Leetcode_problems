class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = Counter(s)
        seen = set()
        stack = []

        for i in range(len(s)):
            while stack and ord(stack[-1]) > ord(s[i]) and freq[stack[-1]] > 0 and s[i] not in seen:
                seen.remove(stack[-1])
                stack.pop()
            
            if s[i] not in seen:
                stack.append(s[i])
                seen.add(s[i])
            freq[s[i]] -= 1

            print(stack)
        
        return "".join(stack)    

