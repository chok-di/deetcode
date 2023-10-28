class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_n = mean * (n+len(rolls)) - sum(rolls)
        a,b =divmod(sum_n,n)
        if a < 1 or a > 6 or (a == 6 and b > 0):
            return []
        res = [a] * n
        for i in range(0,b):
            res[i] += 1
        return res
        