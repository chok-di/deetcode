class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_m = {}
        for number in nums:
            if number in hash_m:
                return True
            hash_m[number] = True
        return False
        