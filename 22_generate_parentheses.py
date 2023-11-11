class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def generate(s,l,r):
            if l == n and r == n:
                ans.append(s)
                return
            if l < n:
                sl = s + "("
                generate(sl,l+1,r)
            if r < l:
                sr = s + ")" 
                generate(sr,l,r+1)
        generate("",0,0)
        return ans