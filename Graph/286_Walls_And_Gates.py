from collections import deque


##bfs
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS,COLS = len(rooms),len(rooms[0])
        visited = set()
        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))

        def addRoom(x,y):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or (x,y) in visited or rooms[x][y] == -1:
                return
            visited.add((x,y))
            q.append((x,y))
            return

        distance = 0
        while q:
            for i in range(len(q)):
                x,y = q.popleft()
                rooms[x][y] = distance
                addRoom(x+1,y)
                addRoom(x-1,y)
                addRoom(x,y+1)
                addRoom(x,y-1)
            distance += 1

##dfs
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS,COLS = len(rooms),len(rooms[0])
        visited = set()
        def dfs(x,y):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or rooms[x][y] == -1 or (x,y) in visited:
                return 2147483647
            if rooms[x][y] == 0:
                return 0
            visited.add((x,y))
            res = min(dfs(x+1,y),dfs(x-1,y),dfs(x,y-1),dfs(x,y+1)) + 1
            visited.remove((x,y))
            return min(res,2147483647)
        for x in range(ROWS):
            for y in range(COLS):
                if rooms[x][y] == 2147483647:
                    rooms[x][y] = dfs(x,y)
        return