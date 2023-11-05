class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        #odd
        for i in range(len(s)):
            l = 0
            while i - l- 1 >= 0 and i + l + 1 < len(s) and s[i - l - 1] == s[i+ l + 1]:
                l += 1
            if 2*l + 1 > len(ans):
                ans = s[i - l:i + l + 1]
        #even
        for i in range(len(s)):
            l = 0
            if i+1 < len(s) and s[i] == s[i+1]:
                while i - l - 1 >= 0 and i+l+2 < len(s) and s[i-l-1] == s[i+l+2]:
                    l += 1
                if 2*l + 2 > len(ans):
                    ans = s[i-l:i+l+2]

        return ans
        