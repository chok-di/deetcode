class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            sum = 0
            for pile in piles:
                sum += math.ceil(pile/mid)
            if sum > h:
                left = mid + 1
            else:
                right = mid - 1

        return left