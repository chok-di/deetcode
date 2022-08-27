class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,ans = 0,0
        charSet = set()
        for right in range(0,len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            ans = max(right - left + 1, ans)
        return ans