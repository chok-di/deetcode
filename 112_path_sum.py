# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.ans = False
        def dfs(node,s):
            if not node.left and not node.right and s + node.val == targetSum:
                self.ans = True
                return
            if node.left:
                dfs(node.left, s+node.val )
            if node.right:
                dfs(node.right,s + node.val)
            return
        dfs(root,0)
        return self.ans
