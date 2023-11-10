class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = inf
        for p1 in range(0,len(nums) - 2):
            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                continue
            p2,p3 = p1 + 1, len(nums) - 1
            while p2 < p3:
                new_sum = nums[p1] + nums[p2] + nums[p3]
                if abs(new_sum - target) < abs(ans - target):
                    ans = new_sum
                if new_sum == target:
                    return ans
                if new_sum > target:
                    p3 -= 1
                if new_sum < target:
                    p2 += 1
        return ans