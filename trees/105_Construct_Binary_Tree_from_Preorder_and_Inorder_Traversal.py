# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        head = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        inorder_left = inorder[:mid]
        inorder_right = inorder[mid + 1:]
        preorder_left = preorder[1:mid+1]
        preorder_right = preorder[mid + 1:]
        head.left = self.buildTree(preorder_left,inorder_left)
        head.right = self.buildTree(preorder_right,inorder_right)
        return head