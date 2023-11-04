class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        prefix = [reward1[i] - reward2[i] for i in range(len(reward1))]
        prefix.sort(reverse=True)
        ans = sum(reward2)
        for i in range(k):
            ans += prefix[i]
        return ans
