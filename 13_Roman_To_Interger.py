class Solution:
    def romanToInt(self, s: str) -> int:
        ans =0
        convertion = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        for i in range(len(s)):
            if i+1 < len(s) and convertion[s[i+1]] > convertion[s[i]]:
                ans -= convertion[s[i]]
            else:
                ans += convertion[s[i]]
        return ans