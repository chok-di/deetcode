# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,min,max):
            if not root:
                return True
            if root.val <= min or root.val >= max:
                return False
            return dfs(root.right,root.val,max) and dfs(root.left,min,root.val)
        return dfs(root,-float('inf'),flo