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
