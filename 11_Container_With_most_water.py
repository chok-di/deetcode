class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height) - 1
        maxl,maxr = 0,0
        ans = 0
        while l < r:
            maxl = max(maxl,height[l])
            maxr = max(maxr,height[r])
            ans = max(min(maxl,maxr) * (r-l),ans)
            if maxl <= maxr:
                l += 1
            else:
                r -= 1
        return ans