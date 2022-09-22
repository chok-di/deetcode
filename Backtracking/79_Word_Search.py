class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])
        visited = set()
        def search(i,j,index):
            if index == len(word):
                return True
            if (i >= rows
                or j >= cols
                or min(i,j) < 0 
                or (i,j) in visited
                or board[i][j] != word[index]):
                    return False
            visited.add((i,j))
            res = (search(i+1,j,index + 1) or search(i - 1, j, index + 1) or search(i,j + 1, index + 1) or search(i, j - 1, index + 1))
            visited.remove((i,j))
            return res
                    
                
        for i in range(rows):
            for j in range(cols):
                if search(i,j,0):
                    return True
        return False