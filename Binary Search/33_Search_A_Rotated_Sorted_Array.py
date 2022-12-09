class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums) - 1
        while left <= right:
            print(left,right)
            mid = (left + right) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            if nums[mid] > target and nums[mid] >= nums[0] and target >= nums[0]:
                right = mid - 1
            elif nums[mid] > target and nums[mid] >= nums[0] and target < nums[0]:
                left = mid + 1
            elif nums[mid] > target and nums[mid] < nums[0]:
                right = mid - 1
            elif nums[mid] < target and nums[mid] >= nums[0]:
                left = mid + 1
            elif nums[mid] < target and nums[mid] < nums[0] and target < nums[0]:
                left = mid + 1
            elif nums[mid] < target and nums[mid] < nums[0] and target >= nums[0]:
                right = mid - 1
        return -1