class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memory = {}
        def dfs(amount,i):
            print(amount,i)
            if i == len(nums):
                return 1 if amount == target else 0
            if(amount,i) in memory:
                return memory[(amount,i)]
            res = dfs(amount + nums[i], i+1) + dfs(amount - nums[i], i+1)
            memory[(amount,i)] = res
            return res
        res = dfs(0,0)
        return res