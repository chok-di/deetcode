class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        rows = abs(fy - sy) + 1
        cols = abs(fx - sx) + 1
        min_time = max(rows,cols) - 1
        if not (rows == 1 and cols == 1):
            return True if t >= min_time else False
        else:
            return True if t != 1 else False
       
        