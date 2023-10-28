class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        memo = set()
        for number in nums:
            if number in memo:
                memo.remove(number)
            else:
                memo.add(number)
        for number in memo:
            return number