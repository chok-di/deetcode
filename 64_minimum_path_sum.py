class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.ans =inf
        last = grid[rows-1][cols-1]
        dp = {}
        dp[(rows-1,cols-1)] = last
        def fn(r,c):
            if (r,c) in dp:
                return dp[(r,c)]
            if r >= rows or c >= cols:
                return inf
            go_right = fn(r,c+1) + grid[r][c]
            go_down = fn(r+1,c) + grid[r][c]
            res = min(go_right,go_down)
            dp[(r,c)] = res
            return res
        return fn(0,0)