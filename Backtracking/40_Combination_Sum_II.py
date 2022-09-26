class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []
        def backtrack(n):
            if sum(subset) == target:
                res.append(subset[::])
                return
            if sum(subset) > target or n ==len(candidates):
                return
            subset.append(candidates[n])
            backtrack(n+1)
            subset.pop()
            while n+1 < len(candidates) and candidates[n+1] == candidates[n]:
                n += 1
            backtrack(n+1)
        backtrack(0)
        return res