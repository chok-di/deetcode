class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left,right = 0,0
        ans = 0
        while right < len(s):
            if s[right] in seen:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1
                right += 1
            elif s[right] not in seen:
                seen.add(s[right])
                ans = max(right - left + 1,ans)
                right += 1
        return ans