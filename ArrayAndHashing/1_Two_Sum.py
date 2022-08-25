class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_m = {}
        for i in range(0,len(nums)):
            if nums[i] in hash_m:
                return [hash_m[nums[i]], i]
            else:
                hash_m[target - nums[i]] = i