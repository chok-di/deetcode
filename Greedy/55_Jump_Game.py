#Greedy algorithm is 10 times faster than the solution commented out

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last:
                last = i
            if last == 0:
                return True
        return False

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         can_reach = [False] * len(nums)
#         can_reach[0] = True
#         for i in range(0,len(nums)):
#             if can_reach[i]:
#                 for j in range(i, min(i+nums[i] + 1, len(nums))):
#                     can_reach[j] = True
#                     if can_reach[len(nums) - 1]:
#                         return True
#         return False