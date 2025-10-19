class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets = []

        def backtrack(ope, clos, path):
            if ope == clos == n:
                brackets.append("".join(path))
                return
            
            if ope == clos:
                path.append("(")
                backtrack(ope + 1, clos, path)
                path.pop()
                return
            
            if ope == n:
                path.append(")")
                backtrack(ope, clos + 1, path)
                path.pop()
            else:
                path.append("(")
                backtrack(ope + 1, clos, path)
                path.pop()
                path.append(")")
                backtrack(ope, clos + 1, path)
                path.pop()

        backtrack(0, 0, [])

        return brackets

