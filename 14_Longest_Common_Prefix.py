class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        i = 0
        findNext = True
        while findNext:
            c=""
            for s in strs:
                if i >= len(s):
                    findNext = False
                    break
                elif not c:
                    c = s[i]
                elif s[i] != c:
                    findNext = False
                    break
            if findNext:
                ans += c
                i += 1
        return ans