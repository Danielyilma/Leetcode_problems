# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
                -10
            9       20
            
                15      7
            
        sum = -1
        -10 -> 9
        
        15 + 20, 7 + 20, 15 + 7 + 20
        
        res = 42
        
        max(left + node, right + node, left + right + node)
        
                1
            2       3
            
        """
        
        res = float("-inf")
        def traverse(root) -> int:
            nonlocal res
    
            if root is None:
                return 0
            
            left_sum = max(traverse(root.left), 0)
            right_sum = max(traverse(root.right), 0)
            
            res = max(left_sum + root.val, right_sum + root.val, left_sum + root.val + right_sum, res)
            # res = max(res, left_sum, right_sum)
            
            
            return max(left_sum + root.val, right_sum + root.val)
        
        traverse(root)   
        return res