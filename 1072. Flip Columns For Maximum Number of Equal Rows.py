class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = {}
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            pattern = ""
            for c in range(cols):
                pattern += str(matrix[r][c])
            if pattern in patterns:
                patterns[pattern] += 1
            else:
                patterns[pattern] = 1
        res = 1
        for pattern,count in patterns.items():
            match_pattern = ""
            same = count
            for c in pattern:
                new_c = "0" if c == "1" else "1"
                match_pattern += new_c
            if match_pattern in patterns:
                same += patterns[match_pattern]
            res = max(res,same)
        return res