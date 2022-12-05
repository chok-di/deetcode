class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        stack = [] #（arrival time)
        pairs = [(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse=True)
        for p,s in pairs:
            eta = (target - p)/s
            if stack and eta <= stack[-1]:
                continue
            stack.append(eta)
        return len(stack)
        