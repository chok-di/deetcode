class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1Count,s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1
            
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        start = 0
        while start < len(s2) - len(s1):
            if matches == 26:
                return True
            startIndex = ord(s2[start]) - ord("a")
            s2Count[startIndex] -= 1
            if s2Count[startIndex] == s1Count[startIndex]:
                matches += 1
            elif s2Count[startIndex] + 1 == s1Count[startIndex]:
                matches -= 1
            start += 1
            endIndex = ord(s2[start + len(s1) - 1]) - ord("a")
            s2Count[endIndex] += 1
            if s2Count[endIndex] == s1Count[endIndex]:
                matches += 1
            elif s2Count[endIndex] - 1 == s1Count[endIndex]:
                matches -= 1
            
        return matches == 26
            
        
            
            
        