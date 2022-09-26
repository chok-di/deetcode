def solution(area):
  curPath = set()
  dp = {}  
  def goForward(i,j):
   
    if area[i][j] == 9:
      return 0#hit the target 
    if (i,j) in curPath or area[i][j] == 0 or i < 0 or i >= len(area )or j < 0 or j >= len(area[0]):
      return float('inf') 

    if (i,j) in dp:
      return dp[(i,j)] #always be the best way to reach destination from (i,j)
      
    curPath.add((i,j))
    best = 1 + min(goForward(i,j+1),goForward(i+1,j), goForward(i-1,j),goForward(i,j-1))
    dp[(i,j)] = best
    curPath.remove((i,j))

    return best 
  return goForward(0,0) # recursively go in all four directions

print("haha")
print (solution([[1,1,1],
 [1,1,1],
 [1,9,1]]
))