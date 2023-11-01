class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dictionary = Counter(nums)
        ans = 0
        for number,count in dictionary.items():
            ans += count * (count-1) // 2
        return ans

        