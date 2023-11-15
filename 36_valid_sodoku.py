class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        sub= defaultdict(list)
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    subx = r // 3
                    suby = c // 3
                    if num in rows[r] or num in cols[c] or num in sub[(subx,suby)]:
                        return False
                    rows[r].append(num)
                    cols[c].append(num)
                    sub[(subx,suby)].append(num)
        return True