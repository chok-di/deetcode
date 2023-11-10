class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zz = [["" for i in range(len(s))] for i in range(numRows)]
        zig = False
        r,c = 0,0

        for i in range(len(s)):
            if r == numRows - 1 or r == 0:
                zig = not zig
            zz[r][c] = s[i]
            if zig:
                r += 1
            if not zig:
                r -= 1
                c += 1
        ans = "".join(["".join(row) for row in zz])
        return ans