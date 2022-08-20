#implement pow(x,n)
#recursion
#Fast Power Algorithm: https://en.wikipedia.org/wiki/Exponentiation_by_squaring
class Solution:
    def fastPow(self,x,n):
        if n == 0:
            return 1
        half = self.fastPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
        
    def myPow(self,x: float, n: int) -> float:
        return self.fastPow(x,n)