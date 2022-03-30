# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        
        #now we want to get the height of the left side 
        def lheight(node):
            if not node: return 0
            return 1+lheight(node.left)# only to return us the left side
        # we want to get the height of the right side
        def rheight(node):
            if not node: return 0
            return 1+rheight(node.right)
        # we have the left and right height we call our root 
        l, r = lheight(root), rheight(root)
        
        #check if the tree is balanced
        # if it's not balacned we call the function right can not be bigger than left 
        if l > r:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
        # 2 to the power of either left or right - the current node 
        else:
            return(2**l)- 1
            
        
        
        
        