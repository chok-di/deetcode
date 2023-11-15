class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for c in range(n)] for r in range(m)]
        matrix[0][0] = 1
        for i in range(m):
            for j in range(n):
                top = matrix[i-1][j] if i - 1 >= 0 else 0
                left = matrix[i][j-1] if j - 1 >= 0 else 0
                matrix[i][j] += top + left
        return matrix[m-1][n-1]