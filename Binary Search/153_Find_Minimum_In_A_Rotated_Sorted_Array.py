class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]
        if len(nums) > 1 and nums[-1] < nums[-2] and nums[-1] < nums[0]:
            return nums[-1]
        left,right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if (mid < len(nums) - 1 and nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]) :
                return nums[mid]
            if nums[mid] >= nums[0]:
                left = mid + 1
            if nums[mid] < nums[0]:
                right = mid - 1