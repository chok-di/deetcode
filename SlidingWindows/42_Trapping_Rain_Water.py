# I made left and right pointer both start from 0, failed some case
# It makes sense to use sliding window, because rain can only be trapped in the hollow lands between two higher pillars
# Should have analyzed the situation more accurately before coding
class Solution:
    def trap(self, height: List[int]) -> int:
        left,right,rain = 0, len(height) - 1, 0
        leftMax,rightMax = height[left],height[right]
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                rain += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                rain += rightMax - height[right]
        return rain