class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = ""

        for st in s:
            if st == "[":
                stack.append(num)
                num = ""
                continue
            elif st == "]":
                temp = ""
                while not stack[-1].isnumeric():
                    temp = stack.pop() + temp
                num1 = int(stack.pop())
                stack.append(temp * num1)
            elif st.isdigit():
                num += st
            else:
                stack.append(st)
        
        return "".join(stack)