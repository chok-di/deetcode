class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hash_m = Counter(words)
        ans = 0
        center = False
        print(hash_m)
        for word,freq in hash_m.items():
            if word[0] == word[1]:
                if freq % 2 == 0:
                    ans += 2 * freq
                elif freq % 2 == 1:
                    ans += 2 * (freq - 1)
                    center = True
            elif word[0] < word[1]:
                ans += 4 * min(hash_m[word[0]+word[1]],hash_m[word[1] + word[0]])
        if center:
            ans += 2
        return ans
