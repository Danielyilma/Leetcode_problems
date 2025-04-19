# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = []

        def dfs(root):
            count = 0
        
            if not root:
                return 0
            
            count += dfs(root.left)
            count += dfs(root.right)

            if root.val == p.val or root.val == q.val:
                count += 1

            if count == 2:
                res.append(root)
                count = 0
            
            return count

        dfs(root)
        return res[0]
