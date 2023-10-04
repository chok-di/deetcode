class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        dp["0"] = 0
        def decode(s):
            print(s)
            if len(s) == 0:
                return 1
            if s in dp:
                return dp[s]
            # single digit
            if len(s) == 1:
                dp[s] = 1
                return 1
     
            oneback,twoback = 0,0
            #last 1 digit:
            if s[-1] != "0":
                oneback = decode(s[:-1])
            #last 2 digit:
            if s[-2] == "1" or (s[-2] == "2" and s[-1] in ["0","1","2","3","4","5","6"]):
                twoback = decode(s[:-2])
            dp[s] = oneback + twoback
            return dp[s]

        return decode(s)