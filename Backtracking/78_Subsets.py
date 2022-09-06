# Will return a list of empty array without .copy() in line 8 lmao
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        def dfs(n):
            if n >= len(nums):
                ans.append(subset.copy())
                return
            subset.append(nums[n])
            dfs(n+1)
            subset.pop()
            dfs(n+1)
        dfs(0)
        return ans