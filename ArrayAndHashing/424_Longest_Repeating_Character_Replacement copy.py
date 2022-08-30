class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        mostFreq = 0
        ans = 0
        left = 0
        for right in range(0,len(s)):
            count[s[right]] = count.get(s[right],0) + 1 
            mostFreq = max(mostFreq, count[s[right]])
            if right - left + 1 - mostFreq > k:
                count[s[left]] -= 1
                left += 1
            ans = max(0,right - left + 1)
        return ans