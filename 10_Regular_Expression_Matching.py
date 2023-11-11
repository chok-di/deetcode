class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #"x*"   "."  ".*"
        # .*
        self.ans = False

        def trim(p):
            newp = ""
            i = 0
            while i < len(p):
                if i < len(p) - 1 and p[i+1] == "*" and p[i:i+2] == newp[:-2]:
                    i += 2
                    continue
                newp += p[i]
                i += 1
            return newp
        
        p = trim(p)


        def superMatch(s,p):
            if p == ".*":
                self.ans = True
                return
            for i in range(len(s) + 1):
                match(s[i:],p[2:])

        def pairMatch(s,p):
            i = 0
            match(s,p[2:])
            while i < len(s) and s[i] == p[0]:
                i += 1
                match(s[i:],p[2:])   
            return
            
        def normalMatch(s,p):
            return match(s[1:],p[1:])
            
        
        def match(s,p):
            if s == p:
                self.ans = True
                return
            if s and not p:
                return
            if len(p) >= 2 and p[:2] == ".*":
                superMatch(s,p)
            elif len(p) >= 2 and p[1] == "*":
                pairMatch(s,p)
            elif s and p and (s[0] == p[0] or p[0] == "."):
                normalMatch(s,p)
        match(s,p)
        return self.ans
                