
def largestRectangleArea(heights):
        maxArea = 0
        stack = []  # pair: (index, height)
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index,height = stack.pop()
                maxArea = max(maxArea, (i - index) * height)
                start = index
            stack.append([start,h])
        for i,h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        return maxArea

print(largestRectangleArea([1,2,3,4,5]))