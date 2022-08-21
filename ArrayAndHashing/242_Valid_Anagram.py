#.get() is useful ^_^

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counter,t_counter = {},{}
        for i in range(0,len(s)):
            s_counter[s[i]] = 1 + s_counter.get(s[i] , 0)
            t_counter[t[i]] = 1 + t_counter.get(t[i], 0)
        for letter in s_counter:
            if s_counter[letter] != t_counter.get(letter, 0):
                return False
        return True