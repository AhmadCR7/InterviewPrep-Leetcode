# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        
        while q:
            node = q.popleft()
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)
        return node.val
'''
we can use level order traversal with que
we do it from right to left and the last node that is left will be the most left node in the tree
we use double ended que or deque 
we add from bot side of the que 
we pop from most left side 
we put its children to the que 
an pop the left again 
we add the right node first bc we want to pop the right first 

'''