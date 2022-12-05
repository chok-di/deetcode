class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #[temp,index]
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackIndex = stack.pop()[1]
                res[stackIndex] = i - stackIndex
            stack.append([temp,i])
        return res
        x