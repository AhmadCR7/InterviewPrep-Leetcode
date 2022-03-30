# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None 
        
        def dfs(node):
            if not node:
                return False 
            left = dfs(node.left)
            right = dfs(node.right)
            curr = node==p or node==q
            if(left and right) or (curr and right) or (curr and left):
                self.ans = node 
                return 
            return left or right or curr
        dfs(root)
        return self.ans
    
    #time complexity is O(n)N is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.
    #space complexity is O(n) his is because the maximum amount of space utilized by the recursion stack would be NN since the height of a skewed binary tree could be NN.
            