class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
 
        for i in range(0,len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            s = set()
            marker = -inf
            for j in range(i+1,len(nums)):
                if nums[j] == marker:
                    continue
                res = target - nums[j]
                if nums[j] in s:
                    ans.append([nums[i],res,nums[j]]) 
                    s.remove(nums[j])
                    marker = res
                elif res >= nums[j]:
                    s.add(res)
        return ans
            