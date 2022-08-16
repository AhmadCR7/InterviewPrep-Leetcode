# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.best = 1
        
        def depth(root):
            if not root:
                return 0
            ansL = depth(root.left)
            ansR = depth(root.right)
            self.best = max(self.best, ansL + ansR + 1)
            return 1 + max(ansL, ansR)
        depth(root)
        return self.best-1
    
    
'''
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
        
SOlutioh 2: 
def diameterOfBinaryTree(self, root):
    self.best = 1
    def depth(root):
        if not root: return 0
        ansL = depth(root.left)
        ansR = depth(root.right)
        self.best = max(self.best, ansL + ansR + 1)
        return 1 + max(ansL, ansR)
        
    depth(root)
    return self.best - 1
            
'''
            
            
        
        