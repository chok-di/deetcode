class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = 0
        i = 0
        while i < len(s):
            if s[i] == 'X':
                ans += 1
                i += 3
            else:
                i += 1
        return ans