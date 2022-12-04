class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        sub_dict = defaultdict(set)
        for i in range(0,9):
            for j in range(0,9):
                sub_num = (i // 3) * 3 + (j//3)  + 1
                val = board[i][j]
                if val == ".":
                    continue
                if (val in row_dict[i] or
                   val in col_dict[j] or
                    val in sub_dict[sub_num]):
                    return False;
                row_dict[i].add(val)
                col_dict[j].add(val)
                sub_dict[sub_num].add(val)
        return True