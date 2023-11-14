class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        for p1 in range(len(nums) - 3):
            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                continue
            for p2 in range(p1+1,len(nums)-2):
                if p2 -1 > p1 and nums[p2] == nums[p2 - 1]:
                    continue
                p3,p4 = p2+1,len(nums) - 1
                while p3 < p4:
                    if p3 - 1 > p2 and nums[p3] == nums[p3 - 1]:
                        p3 += 1
                        continue
                    if p4 < len(nums) - 1 and nums[p4] == nums[p4 + 1]:
                        p4 -= 1
                        continue
                    if nums[p1] + nums[p2] + nums[p3] + nums[p4] == target:
                        ans.append([nums[p1],nums[p2],nums[p3],nums[p4]])
                        p3 += 1
                        p4 -= 1
                        continue
                    if nums[p1] + nums[p2] + nums[p3] + nums[p4] > target:
                        p4 -= 1
                        continue
                    if nums[p1] + nums[p2] + nums[p3] + nums[p4] < target:
                        p3 += 1
        return ans