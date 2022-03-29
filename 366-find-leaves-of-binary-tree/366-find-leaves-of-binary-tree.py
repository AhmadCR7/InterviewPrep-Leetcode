# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        #creating out dic
        res = collections.defaultdict(list)
        
        
       #post order
        def dfs(node, layer):
            if not node:
                return layer
            
            left = dfs(node.left, layer)
            right = dfs(node.right, layer)
            
            layer = max(left, right)
            
            res[layer].append(node.val)
            
            return layer + 1
        dfs(root, 0)
        
        return res.values()
    
#{
#  0: [4,5,3],
#  1: [2],
#  2: [1]
#
#}
#
#
#

    
    
        