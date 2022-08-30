class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        hash_m = {}
        freq = [[]  for i in range (0,len(nums))]
        for number in nums:
            hash_m[number] = hash_m.get(number,0) + 1
        for number,count in hash_m.items():
            freq[count - 1].append(number)
        for i in range (len(nums) - 1, -1, -1):
            for number in freq[i]:
                ans.append(number)
                if len(ans) == k:
                    return ans