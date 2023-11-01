class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        def findNext(n):
            if n > high or len(str(n)) > 9:
                return
            if n >= low:
                ans.append(n)
            if str(n)[-1] == '9':
                new_str =""
                for i in range(1,len(str(n))+2):
                    new_str += str(i)
                new_num = int(new_str)
                findNext(new_num)
            else:
                new_digit = str(int(str(n)[-1]) + 1)
                new_str = str(n)[1:] + new_digit
                new_num = int(new_str)
                findNext(new_num)
        start = ""
        for i in range(1,len(str(low)) + 1):
            start += str(i)
        start_num = int(start)
        findNext(start_num)
        return ans
