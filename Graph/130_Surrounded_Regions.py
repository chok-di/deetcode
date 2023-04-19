class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        visited = set()
        def flip(x,y):
            if x < 0 or x > len(board) - 1 or y < 0 or y > len(board[0]) - 1 or (x,y) in visited or board[x][y] == "X":
                return
            if (x == 0 or x == len(board) - 1 or y ==0 or y == len(board[0]) - 1) and board[x][y] == "O":
                return False
            visited.add((x,y))
            adjacents = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            for (next_x,next_y) in adjacents:
                if flip(next_x,next_y) == False:
                    visited.remove((x,y))
                    return False
            visited.remove((x,y))
            return True


        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == "O" and flip(x,y) == True:
                    board[x][y] = 'X'
        return board