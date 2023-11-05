class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        L,n = 10,len(s)
        if n <= L:
            return []
        PRIME = 4
        h = 0
        seen= set()

        to_int = {"A":1,"G":2,"C":3,"T":4}
        PRIME = 5
        
        for i in range(len(s)):
            if i < 10:
                h += pow(4,(9-i)) * to_int[s[i]]
            
            else:
                if i == 10:
                    seen.add(h)
                h = h * 4 - pow(4,10) * to_int[s[i-10]] + to_int[s[i]]
                if h in seen:
                    ans.add(s[i-9:i+1])
                seen.add(h)
        return ans