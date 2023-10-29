class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_v = 0
        for element in strs:
            if element.isnumeric():
                val = int(element)
            else:
                val =len(element)
            max_v= max(max_v,val)
        return max_v


        