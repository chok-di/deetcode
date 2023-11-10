class Solution:
    def reverse(self, x: int) -> int:
        ##stop before overflow
        INT_MAX = pow(2,31) - 1
        ans = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x > 0:
            x,d = divmod(x,10)
            if ans < (INT_MAX - d)/10:
                ans = ans * 10 + d
            else:
                ans = 0
                break
        return ans * sign