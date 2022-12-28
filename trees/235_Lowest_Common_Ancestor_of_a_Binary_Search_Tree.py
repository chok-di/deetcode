class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        pval,qval = p.val,q.val
        while curr:
            if curr.val > max(pval,qval):
                curr = curr.left
                continue
            elif curr.val < min(pval,qval):
                curr = curr.right
                continue
            return curr# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        res = []
        q.append(root)
        while q:
            val = []
            width = len(q)
            for i in range(width):
                curr = q.popleft()
                val.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(val)
        return res
            