class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(row,col):
            if (row not in range(rows) 
            or col not in range(cols) 
            or grid[row][col] == '0' 
            or (row,col) in visited):
                return
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            visited.add((row,col))
            for (dr,dc) in directions:
                dfs(row + dr, col + dc)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row,col) not in visited:
                    islands += 1
                    dfs(row,col)
        return islands