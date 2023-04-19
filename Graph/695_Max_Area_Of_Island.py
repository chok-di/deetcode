class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(x,y):
            if min(x,y) < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0 or (x,y) in visited:
                return 0
            visited.add((x,y))
            res = dfs(x,y+1) + dfs(x,y-1) + dfs(x+1,y)+ dfs(x-1,y) + 1
            return res
        max_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_island = max(dfs(i,j),max_island)
        return max_island