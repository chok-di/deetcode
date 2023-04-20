class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS,COLS = len(grid), len(grid[0])

        def rot(x,y):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or grid[x][y] == 0:
                return
            if grid[x][y] == 1:
                global has_fresh
                has_fresh = True
                return 
            if grid[x][y] == 2:
                adjacents = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
                for(next_x,next_y) in adjacents:
                    if next_x >=0 and next_x < ROWS and next_y >= 0 and next_y < COLS and grid[next_x][next_y] == 1:
                        global has_change
                        has_change = True
                        print(next_x,next_y)
                        grid[next_x][next_y] = 1.5

        
        while True:
            global has_fresh
            has_fresh = False
            global has_change
            has_change = False
            for x in range(ROWS):
                for y in range(COLS):
                    if grid[x][y] == 1.5:
                        grid[x][y] = 2   
            for x in range(ROWS):
                for y in range(COLS):
                    rot(x,y)    
            if not has_change and has_fresh:
                print(grid)
                return -1
            if not has_change:
                break
            res += 1
        return res