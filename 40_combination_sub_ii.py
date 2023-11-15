class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def fn(sub_set,i):
            if sum(sub_set) == target:
                ans.append(sub_set)
                return
            if i >= len(candidates):
                return
            if sum(sub_set) > target:
                return
            if target - sum(sub_set) < candidates[i]:
                return
            next_i = i+1
            while next_i < len(candidates) and candidates[next_i] == candidates[next_i - 1]:
                next_i += 1
            has_i = sub_set.copy()
            for j in range(next_i - i):
                has_i.append(candidates[i])
                fn(has_i.copy(),next_i)
            fn(sub_set,next_i)
        fn([],0)
        return ans