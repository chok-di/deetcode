class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def getNum(row,col):
            if col == 0 or row == col:
                return 1
            return getNum(row - 1, col - 1) + getNum(row - 1, col)
        ans = []
        for i in range(0, rowIndex + 1):
            ans.append(getNum(rowIndex, i))
        return ans