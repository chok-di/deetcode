class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        #stk represents ppl who are not blocked yet
        stk = []
        for i,h in enumerate(heights):
            while stk and h >= heights[stk[-1]]:
                ans[stk.pop()] += 1
            if(stk):
                ans[stk[-1]] += 1
            stk.append(i)
        return ans
           