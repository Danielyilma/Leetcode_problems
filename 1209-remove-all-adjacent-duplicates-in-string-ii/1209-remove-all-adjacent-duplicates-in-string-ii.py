class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        count = []

        for st in s:
            if stack and stack[-1] == st:
                count[-1] += 1
                if count[-1] == k:
                    stack.pop()
                    count.pop()
            else:
                stack.append(st)
                count.append(1)
            
        result = ""
        for i in range(len(stack)):
            result += (stack[i] * count[i])
        
        return result
