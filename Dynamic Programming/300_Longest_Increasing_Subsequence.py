class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1
        arr = [1] * len(nums)
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    arr[i] = max(arr[i],arr[j] + 1)
            res = max(res, arr[i])
        return res
            