class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1
        leftr,rightr = 0,rows
        leftc,rightc = 0,cols
        while leftr <= rightr:
            midr = (leftr + rightr) // 2
            if matrix[midr][cols] < target:
                leftr = midr + 1
            elif matrix[midr][0] > target:
                rightr = midr - 1 
            else:
                while leftc <= rightc:
                    midc = (leftc + rightc) // 2
                    if matrix[midr][midc] == target:
                        return True
                    elif matrix[midr][midc] > target:
                        rightc = midc - 1
                    else:
                        leftc = midc + 1
                return False
        return False
            