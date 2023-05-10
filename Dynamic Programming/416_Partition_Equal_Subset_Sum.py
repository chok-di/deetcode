class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half = sum(nums)/2
        def dfs(index,target):
            if target == 0:
                return True
            if target < 0 or index == len(nums):
                return False
            ##include this number
            return dfs(index+1,target - nums[index]) or dfs(index+1,target)
        return dfs(0,half)