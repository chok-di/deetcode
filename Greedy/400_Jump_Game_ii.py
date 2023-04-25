class Solution:
    def jump(self, nums: List[int]) -> int:
        time = [float('inf')] * len(nums)
        time[0] = 0
        for i in range(len(nums)):
            for j in range(i+1, min(i+nums[i]+1,len(nums))):
                time[j] = min(time[j],time[i] + 1)
        return time[-1]