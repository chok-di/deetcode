class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right,mid = 0,len(nums)-1,0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                break
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
        if mid > len(nums) - 1 or nums[mid] != target:
            return [-1,-1]

        l1,r1 = left,mid
        while l1 <= r1:
            mid1 = (l1 + r1) // 2
            if nums[mid1] == target and (mid1 == 0 or nums[mid1 - 1] < target):
                left = mid1
                break
            if nums[mid1] < target:
                l1 = mid1 + 1
            if mid1 > 0 and nums[mid1 - 1] == target:
                r1 = mid1 - 1
        l2,r2 = mid,right
        while l2 <= r2:
            mid2 = (l2 + r2) // 2
            if nums[mid2] == target and (mid2 == len(nums) - 1 or nums[mid2 + 1] > target):
                right = mid2
                break
            if nums[mid2] > target:
                r2 = mid2 - 1
            if nums[mid2 + 1] == target:
                l2 = mid2 + 1
        return[left,right]