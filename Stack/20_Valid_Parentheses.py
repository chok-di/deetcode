#stack: last in first out
#.append(),pop()
class Solution:
    def isValid(self, s: str) -> bool:
        match = {")":"(","]":"[","}":"{"}
        stack = []
        for char in s:
            if char in match:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last!= match[char]:
                    return False
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        return False