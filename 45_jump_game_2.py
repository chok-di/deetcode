class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [inf] * len(nums)
        dp[-1] = 0
        for i in range(len(nums) - 2,-1,-1):
            if i + nums[i] >= len(nums) - 1:
                dp[i] = 1
                continue
            shortest = inf
            for j in range(1,nums[i]+1):
                shortest = min(shortest,1 + dp[i+j])
            dp[i] = shortest
        return dp[0]
                