class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memory = {}
        def dp(amount,i):
            if (amount,i) in memory:
                return memory[(amount,i)]
            if amount == 0:
                return 1
            if amount < 0 or i == len(coins):
                return 0
            res = dp(amount - coins[i],i) + dp(amount,i+1)
            memory[(amount,i)] = res
            return res   
        return dp(amount,0)
            
            
                