# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        curr = root
        q = collections.deque()
        q.append(root)
        while q:
            width = len(q)
            res.append(q[-1].val)
            for i in range(width):
                node = q.pop()
                if node.right:
                    q.appendleft(node.right)
                if node.left:
                    q.appendleft(node.left)
        return res
