class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        def dfs(n):
            if sum(subset) == target:
                ans.append(subset.copy())
                return
            if sum(subset) > target or n >= len(candidates):
                return
            #decision to include candidates[n]
            subset.append(candidates[n])
            dfs(n)
            #decision not to include candidates[n]
            subset.pop()
            dfs(n+1)
        dfs(0)
        return ans