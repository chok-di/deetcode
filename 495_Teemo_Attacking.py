class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        for i in range(len(timeSeries)):
            if i == len(timeSeries) - 1 or timeSeries[i+1] - timeSeries[i] >= duration:
                ans += duration
            else:
                ans += timeSeries[i+1] - timeSeries[i]
        return ans
