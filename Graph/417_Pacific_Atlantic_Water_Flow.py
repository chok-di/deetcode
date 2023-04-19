class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        visited_pacific = set()
        visited_atlantic = set()
        def pacific(x,y,prev):
            if y < 0 or y > len(heights[0]) or (x,y) in visited or heights[x][y] > prev:
                return
            if x == 0 or y == 0:
                return True
            visited_pacific.add((x,y))
            adjacents = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
            for (next_x,next_y) in adjacents:
                if(pacific(next_x,next_y,heights[x][y])):
                    return True
            visited_pacific.remove((x,y))
            return False

        def atlantic(x,y,prev):
            if x < 0 or x > len(heights) or (x,y) in visited or heights[x][y] > prev:
                return
            if x == len(heights) or y == len(heights[0]):
                return True
            visited_atlantic.add((x,y))
            adjacents = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
            for (next_x,next_y) in adjacents:
                if(atlantic(next_x,next_y,heights[x][y])):
                    return True
            return False
        for x in range(heights):
            for y in range(heights[0]):
                if pacific(x,y,math) and atlantic(x,y,0):
                    res.append([x,y])
        return res