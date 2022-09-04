# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        def dfs(root):
            if not root: return 0
            val = root.val + dfs(root.left) + dfs(root.right)
            counter[val] += 1
            return val
        dfs(root)
        max_freq = max(counter.values())
        res = []
        for k in counter:
            if counter[k] == max_freq:
                res.append(k)
        return res