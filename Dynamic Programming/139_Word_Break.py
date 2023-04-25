class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        dp[len(s)] = True
        def dfs(i):
            if i in dp:
                return dp[i]
            for word in wordDict:
                if s[i:i+len(word)] == word and dp[i+len(word)]:
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        for i in range(len(s)-1,-1,-1):
            dfs(i)
        print(dp)
        return dp[0]