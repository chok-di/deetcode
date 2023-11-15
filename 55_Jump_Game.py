 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        distance = 0
        gas = 1
        for i in range(len(nums)):
            distance += 1
            gas = max(gas - 1, nums[i])
            if gas <= 0:
                break
        return distance == len(nums)

            
        