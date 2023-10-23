class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        global sum
        sum = 0
        sub = []
        def dfs(i):
            global sum
            if i == len(nums):
                return
            sub.append(nums[i])
            subsum = reduce(lambda a, c: a ^ c, sub, 0) 
            sum += subsum
            dfs(i+1)
            sub.pop()
            dfs(i+1)
        dfs(0)
        return sum
