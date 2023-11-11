class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        add = [True] * len(nums)
        def fn(sub_set):
            if len(sub_set) == len(nums):
                ans.append(sub_set)
                return
            for i in range(len(nums)):
                if add[i]:
                    new_set = sub_set.copy()
                    new_set.append(nums[i])
                    add[i] = False
                    fn(new_set)
                    add[i] = True
        fn([])
        return ans