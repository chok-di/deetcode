class Solution:
    def intToRoman(self, num: int) -> str:
        convert = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}
        nums = list(convert.keys())
        ans = ""
        for i in range(len(nums)):
            times,num = divmod(num,nums[i])
            if 4 > times > 0:
                ans += times*convert[nums[i]]
            if times == 4:
                partial = convert[nums[i]] 
                if ans and ans[-1] == convert[nums[i-1]]:
                    ans = ans[:-1]
                    partial += convert[nums[i-2]]
                else:
                    partial += convert[nums[i-1]]
                ans += partial 
        return ans
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        def delete(root,prev):
            if not root or not prev:
                return
            if root.val in to_delete:
                delete(root.left,root.left)
                delete(root.right,root.right)
                return
            if root.val == prev.val and prev.val not in to_delete:
                ans.append(root)
            if prev.left:
                if prev.left.val in to_delete:
                    delete(prev.left.left,prev.left.left)
                    delete(prev.left.right,prev.left.right)
                    prev.left = None
                else:
                    delete(root,prev.left)
            if prev.right:
                if prev.right.val in to_delete:
                    delete(prev.right.left,prev.right.left)
                    delete(prev.right.right,prev.right.right)
                    prev.right = None
                else:
                    delete(root,prev.right)
        delete(root,root)
        return ans