class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        
        def dfs(i,j):
            if i == len(word1) and j < len(word2):
                return len(word2) - j
            if j == len(word2) and i < len(word1):
                return len(word1) - i
            if i == len(word1) and j == len(word2):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if word1[i] == word2[j]:
                return dfs(i+1,j+1)
            else:
                replace = dfs(i+1,j+1) + 1
                delete = dfs(i+1,j) + 1
                add = dfs(i,j+1) + 1
                res = min(replace,delete,add)
                dp[(i,j)] = res
                return res
        ans = dfs(0,0)
        print(dp)
        return ans
            