def wire_DHD_SG1(existing_wires):
    wire_list =[list(str) for str in existing_wires.split('\n')]
    row = len(wire_list) - 1
    col = len(wire_list[0]) - 1
    dp = {}
    
    currPath = set()
    bestPath = set()
    bestDistance = float('inf')
    
    def backtrack(i,j):

        if min(i,j) < 0 or i > row or j > col or (i,j) in currPath or wire_list[i][j] == "X":
            return float('inf')
        if wire_list[i][j] == "G":
            if len(bestPath) == 0 or len(bestPath) > len(currPath):
                bestPath.clear()
                bestPath.update(currPath.copy())
            return float('inf')
        if wire_list[i][j] in dp:
            return dp[(i,j)]
        currPath.add((i, j))
        best = min(1 + min(backtrack(i, j + 1),
                       backtrack(i, j - 1), 
                       backtrack(i + 1, j),
                       backtrack(i - 1, j)),
              2**0.5 + min(backtrack(i - 1 , j - 1),
                       backtrack(i - 1, j + 1),
                       backtrack(i + 1, j - 1),
                       backtrack(i + 1, j + 1)))
        currPath.remove((i, j)) 
        dp[(i, j)] = best
        return dp[(i, j)]
    
    for i in range(row + 1):
        for j in range(col + 1):
            if wire_list[i][j] == "S":
                backtrack(i,j)
    if len(bestPath) > 0:
        for path in bestPath:
            if wire_list[path[0]][path[1]] != "S":
                wire_list[path[0]][path[1]] = "P"
            pathed_wire_list = ["".join(list) for list in wire_list]
        return "\n".join(pathed_wire_list)
            
    return "Oh for crying out loud..."

