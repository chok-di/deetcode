class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def fn(s1,s2):
            if(s1,s2) in dp:
                return dp[(s1,s2)]
            if s1 == s2:
                return 0
            if not s1 or not s2:
                res = max(len(s1),len(s2))
                dp[(s1,s2)] = res
                return res
            if s1[0] == s2[0]:
                res = fn(s1[1:],s2[1:])
                dp[(s1,s2)] = res
                return res
            else:
                insert = 1 + fn(s1,s2[1:])
                delete = 1 + fn(s1[1:],s2)
                replace = 1 + fn(s1[1:],s2[1:])
                res = min(insert,delete,replace)
                dp[(s1,s2)] = res
                return res
        fn(word1,word2)
        return fn(word1,word2)