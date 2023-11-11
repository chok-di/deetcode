class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        add = [True] * len(nums)
        def fn(sub_set):
            if len(sub_set) == len(nums):
                ans.append(sub_set)
                return
            for i in range(len(nums)):
                if add[i]:
                    if i > 0 and nums[i] == nums[i-1] and add[i-1]:
                        continue
                    new_set = sub_set.copy()
                    new_set.append(nums[i])
                    add[i] = False
                    fn(new_set)
                    add[i] = True
        fn([])
        return ans