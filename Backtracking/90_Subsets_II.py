class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def backtrack(n):
            if n == len(nums):
                res.append(subset[::])
                return
            subset.append(nums[n])
            backtrack(n+1)
            subset.pop()
            while n+1 < len(nums) and nums[n+1] == nums[n]:
                n += 1
            backtrack(n+1)
        backtrack(0)
        return res
        