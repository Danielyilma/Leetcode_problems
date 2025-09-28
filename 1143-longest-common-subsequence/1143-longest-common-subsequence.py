class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        store = {}

        def backtrack(idx1, idx2):
            result = 0

            if (idx1, idx2) in store:
                return store[(idx1, idx2)]

            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0
            elif text1[idx1] == text2[idx2]:
                result = backtrack(idx1 + 1, idx2 + 1) + 1
            else:
                result = max(backtrack(idx1, idx2 + 1), backtrack(idx1 + 1, idx2))
            
            store[(idx1, idx2)] = result

            return result

        return backtrack(0, 0)