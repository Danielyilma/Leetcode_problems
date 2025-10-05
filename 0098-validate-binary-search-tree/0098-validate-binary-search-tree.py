# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def subValidate(node, minimum, maximum):

            if not node:
                return True
            

            if not (minimum < node.val < maximum):
                return False
            
            isvalid = subValidate(node.left, minimum, node.val)

            if isvalid:
                isvalid = subValidate(node.right, node.val, maximum)
            
            return isvalid
        
        return subValidate(root, float("-inf"), float("inf"))