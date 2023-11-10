class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = {}
        dp[len(nums)] = True
        dp[len(nums) - 1] = False
        #partition starting from index i, assuming that index before is already paritioned out
        def fn(i):
            if i in dp:
                return dp[i]
            p1,p2,p3 = False,False,False
            if nums[i] == nums[i+1] and fn(i+2):
                p1 = True
            if i < len(nums) - 2:
                if nums[i] == nums[i+1] and nums[i] == nums[i+2] and fn(i+3):
                    p2 = True
                if nums[i+1] == nums[i] + 1 and nums[i+2] == nums[i] + 2 and fn(i+3):
                    p3 = True
            res = p1 or p2 or p3
            dp[i] = res
            return res
        return fn(0)