# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        if not root:
            return res
        q = collections.deque()  #[node,max_val]
        q.append([root,root.val])
        res.append(root)
        while q:
            curr = q.popleft()
            if curr[0].left and curr[0].left.val >= curr[1]:
                res.append(curr[0].left)
                q.append([curr[0].left,curr[0].left.val])
            elif curr[0].left and curr[0].left.val < curr[1]:
                q.append([curr[0].left,curr[1]])
            if curr[0].right and curr[0].right.val >= curr[1]:
                res.append(curr[0].right)
                q.append([curr[0].right,curr[0].right.val])
            elif curr[0].right and curr[0].right.val < curr[1]:
                q.append([curr[0].right,curr[1]])
        return len(res)
