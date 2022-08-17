class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # //if only one step: pay it
        # //if only two steps: pay the least
        # //if three steps: first + thrid, or second
        # //if four steps: three steps answers + fourth step, or two steps answers plus thrid
        #if n steps: n-1 cost + nth cost or n-2 cost + (n-1)th cost
            if len(cost) == 1:
                return cost[0]
            if len(cost) == 2:
                return min(cost[0],cost[1])
            if len(cost) == 3:
                return min((cost[0]+ cost[2]), cost[1])
            a,b = min(cost[0],cost[1]), min((cost[0] + cost[2]), cost[1])
            for i in range(4,len(cost) + 1):
                helper = b
                b = min((a + cost[i-2]) , (b + cost[i - 1]))
                a = helper
            return b