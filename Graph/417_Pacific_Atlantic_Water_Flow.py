class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        visited_pacific = set()
        visited_atlantic = set()
        def pacific(x,y,prev):

            if min(x,y) < 0 or x >= len(heights) or y >= len(heights[0]) or (x,y) in visited_pacific or heights[x][y] > prev:
                return
            if [x,y] in res or x == 0 or y == 0:
                return True

            visited_pacific.add((x,y))
            adjacents = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
            for (next_x,next_y) in adjacents:
                if(pacific(next_x,next_y,heights[x][y])):
                    visited_pacific.remove((x,y))
                    return True
            visited_pacific.remove((x,y))
            return False

        def atlantic(x,y,prev):
          
            if min(x,y) < 0 or x >= len(heights) or y >= len(heights[0]) or (x,y) in visited_atlantic or heights[x][y] > prev:
                print("dead")
                return
            if [x,y] in res or x == len(heights) - 1 or y == len(heights[0]) - 1:
                return True
           
            visited_atlantic.add((x,y))
            adjacents = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
            for (next_x,next_y) in adjacents:
                if(atlantic(next_x,next_y,heights[x][y])):
                    visited_atlantic.remove((x,y))
                    return True
            visited_atlantic.remove((x,y))
            return False
        for x in range(len(heights)):
            for y in range(len(heights[0])):
                if pacific(x,y,math.inf) and atlantic(x,y,math.inf):
                    res.append([x,y])
    
        return res