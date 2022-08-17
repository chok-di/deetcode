class Solution:
    def climbStairs(self, n: int) -> int:
        if (n < 3):
            return n;
        a,b = 1,2;
        for i in range(3,n+1):
            helper = b
            b += a
            a = helper
        return b