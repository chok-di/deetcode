class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net = [0] * len(gas)
        for i in range(len(gas)):
            net[i] = gas[i] - cost[i]
        if sum(net) < 0 :
            return -1
        total = 0
        start = 0
        for i in range(len(net)):
            total += net[i]
            if total <0:
                total = 0
                start = i + 1
        return start