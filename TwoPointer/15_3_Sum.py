# too many while loops will cause runtime error. Below is a failure example

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        ans = []
        for one in range(0, len(nums)-2):
            if nums[one] > 0:
                break
            if one > 0:
                if nums[one] == nums[one - 1]:
                    continue
            two = one + 1
            three = len(nums) - 1
            while two < three:
                sum = nums[one] + nums[two] + nums[three]
                if sum == 0:
                    ans.append([nums[one], nums[two], nums[three]])
                    two += 1
                    three -= 1
                    while nums[two] == nums[two - 1] and two < three:
                        two += 1
                elif sum < 0:
                    two += 1
                elif sum > 0:
                    three -= 1
        return ans




# class Solution:
#     def threeSum(nums):
#         nums.sort()
#         one = 0
#         ans = []
#         while one < len(nums) - 2 and nums[one] <= 0:
#             target = - nums[one]
#             two = one + 1
#             three = len(nums) - 1
#             while two < three:
#                 if nums[two] + nums[three] == target:
#                     ans.append([nums[one],nums[two],nums[three]])
#                 elif nums[two] + nums[three] > target:
#                     three -= 1
#                     while nums[three] == nums[three + 1] and two < three:
#                         three -= 1
#                 elif nums[two] + nums[three] < target:
#                     two += 1
#                     while nums[two] == nums[three - 1] and two < three:
#                         two += 1
#             one += 1
#             while (nums[one] == nums[one - 1]):
#                 one += 1
#         print(ans)
#         return ans
#     threeSum([-1,0,1,2,-1,-4])