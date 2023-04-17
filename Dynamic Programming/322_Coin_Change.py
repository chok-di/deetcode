class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0}
        for num in range (1,amount+1):
            if num in coins:
                dp[num] = 1
            else:
                dp[num] = float('inf')
                for coin in coins:
                    if num - coin > 0:
                        dp[num] = min(dp[num - coin] + 1, dp[num])
        return dp[amount] if dp[amount] != float('inf') else -1



