class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i != 0:
            for j in range(len(nums) - 1,i-1,-1):
                if nums[j] > nums[i-1]:
                    temp = nums[i-1]
                    nums[i-1] = nums[j]
                    nums[j] = temp
                    break
        l,r = i,len(nums) - 1
        while l < r:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -= 1