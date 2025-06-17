# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def inorder_successer(node):
            if node.left == None:
                return node

            return inorder_successer(node.left)

        if not root:
            return
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            
            temp = inorder_successer(root.right)
            root.val, temp.val = temp.val, root.val
            root.right = self.deleteNode(root.right, key)
        return root
            

            
            
        


            
