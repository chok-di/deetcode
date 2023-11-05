class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        pointer = 0
        leftmax = nums[0]
        currmax = nums[0]
        for i in range(0,len(nums)):
            currmax = max(currmax,nums[i])
            if nums[i] < leftmax:
                pointer = i
                leftmax = currmax
        return pointer+1
