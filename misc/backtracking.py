def solution(area):
   curPath = set()
   m = len(area)
   n = len(area[0])
   dp = {}

   def goForward(i, j):
       if i < 0 or i >= m or j < 0 or j >= n or (i, j) in curPath or area[i][j] == 0:
           return float('inf')
       if area[i][j] == 9:
           return 0  # hit the target
       if (i,j) in dp:
           return dp[(i,j)]

       # exploring the possible paths
       curPath.add((i, j)) ## when i,j was added, you MUST add (i,j) to th epath
       best = 1 + min(goForward(i, j + 1), goForward(i + 1, j), goForward(i - 1, j), goForward(i, j - 1))
       curPath.remove((i, j)) ##backtracking
       dp[(i, j)] = best  # storing the best
       return dp[(i, j)]
   return goForward(0, 0) if goForward(0,0) != "inf" else -1  

print(solution([[1,0,0],[1,1,1],[1,1,9]]))