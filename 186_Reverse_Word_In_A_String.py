class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(l,r):
            while l < r:
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                l += 1
                r -= 1
        reverse(0,len(s) - 1)
        l,r = 0,0
        while r <= len(s):
            while r < len(s) and s[r] != " ":
                r += 1
            reverse(l,r-1)
            l,r = r+1,r+1     
        return
     