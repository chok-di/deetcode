# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = collections.deque()
        def inorder(root):
            if root:
                inorder(root.left)
                q.append(root)
                inorder(root.right)
                return
        inorder(root)
        return q[k-1].val