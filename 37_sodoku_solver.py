class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solved = False
        rows = defaultdict(list)
        cols = defaultdict(list)
        subs = defaultdict(list)
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                x,y = r//3,c//3
                if num != ".":
                    rows[r].append(num)
                    cols[c].append(num)
                    subs[(x,y)].append(num)

        def solve(r,c):
            if self.solved:
                return
            if r == 9:
                self.solved = True
                return
            if c == 9:
                return solve(r+1,0)
            if board[r][c] != ".":
                return solve(r,c+1)

            possibles = []
            for num in range(1,10):
                s = str(num)
                if s not in rows[r] and s not in cols[c] and s not in subs[(r//3,c//3)]:
                    possibles.append(s)

            if len(possibles) == 0:
                return
            original_r = rows[r].copy()
            original_c = cols[c].copy()
            original_s = subs[(r//3,c//3)].copy()
            for s in possibles:
                board[r][c] = s
                rows[r].append(s)
                cols[c].append(s)
                subs[(r//3,c//3)].append(s)
                solve(r,c+1)
                if self.solved:  
                    return
                board[r][c] = "."
                rows[r] = original_r.copy()
                cols[c] = original_c.copy()
                subs[(r//3,c//3)] = original_s.copy()
        solve(0,0)
        return board