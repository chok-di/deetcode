class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dict = {(m-1,n-1):1}
        def dp(x,y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 0
            if (x,y) in dict:
                return dict[(x,y)]
            res = dp(x+1,y) + dp(x,y+1) 
            dict[(x,y)] = res
            return res
        return dp(0,0)
            