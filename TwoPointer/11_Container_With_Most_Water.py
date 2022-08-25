class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right,max_vol = 0,len(height) - 1,0
        while left < right:
            vol = (right - left) * min(height[left],height[right])
            max_vol = max(max_vol,vol)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_vol