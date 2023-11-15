class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        seen_hash = defaultdict(list)
        for s in strs:
            h = 0
            for c in s:
                i = ord(c) - ord("a") + 1
                h += pow(29,i) + 1
            if h in seen_hash:
                seen_hash[h].append(s)
            if h not in seen_hash:
                seen_hash[h] = [s] 
        return seen_hash.values()