class Solution:
    def countAndSay(self, n: int) -> str:
        def count(s):
            say = ""
            count = 0
            for i in range(len(s)):
                if i == 0 or s[i] == s[i-1]:
                    count += 1
                if i > 0 and s[i] != s[i-1]:
                    say += str(count)
                    say += str(s[i-1])
                    count = 1
                if i == len(s) - 1:
                    say +=str(count)
                    say += str(s[i]) 
            return say
        if n == 1:
            return "1"
        last = "1"
        for i in range(n-1):
            last = count(last)
        return last