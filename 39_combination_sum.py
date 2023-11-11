class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def fn(nums,i,n):
            if n == 0:
                ans.append(nums)
                return
            if i == len(candidates):
                return
            if n < candidates[i]:
                return
            if n > 0:
                nums1 = nums.copy()
                nums1.append(candidates[i])
                fn(nums1,i,n - candidates[i])
                nums2 = nums.copy()
                fn(nums2,i+1,n)
        fn([],0,target)
      
        return ans