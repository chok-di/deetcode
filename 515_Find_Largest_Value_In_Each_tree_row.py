# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans=[root.val]
        s = [root]
        while True:
            children = []
            max_v = -float('inf')
            while s:
                curr = s.pop()
                if curr.left:
                    children.append(curr.left)
                    max_v = max(max_v, curr.left.val)
                if curr.right:
                    children.append(curr.right)
                    max_v = max(max_v,curr.right.val)
            if children:
                ans.append(max_v)
                s = children
            else:
                break
        return ans