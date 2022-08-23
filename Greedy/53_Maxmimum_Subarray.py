#kadane's algorithm, again
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum,currMax = -float("inf"), -float("inf")
        for i in range(0, len(nums)):
            currMax = max(currMax + nums[i], nums[i])
            if currMax > maxSum:
                maxSum = currMax
        return maxSum