class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for big in range(0,len(nums)):
            small,mid = 0,big - 1
            while small < mid and mid < big:
                if nums[small] + nums[mid] > nums[big]:
                    ans += mid - small
                    mid -= 1
                else:
                    small += 1
        return ans
