# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0 
        
        def longestPath(node):
            if not node:
                return 0
            
            nonlocal diameter
            
            leftPath = longestPath(node.left)
            rightPath = longestPath(node.right)
            
            diameter = max(diameter, leftPath + rightPath)
            return max(leftPath, rightPath) + 1
        longestPath(root)
        return diameter 
    
    

            
        
        