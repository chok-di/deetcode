class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                index = ord(letter) - ord("a")
                count[index] += 1
            ans[tuple(count)].append(word)
        return ans.values()
        