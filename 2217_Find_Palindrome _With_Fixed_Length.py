class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        def nextPalindrome(n,num):
            l = len(str(n))
            left = str(n)[:(l+1)//2]
            left_next = str(int(left) + num -1)
            right_next = left_next[::-1][l%2:]
            new_palindrome =  int(left_next + right_next)
            return new_palindrome if len(str(new_palindrome)) == intLength else -1
        first_palindrome = int("1" + "0"*(intLength - 2) + "1") if intLength > 1 else 1
        ans = []
        for i in range(len(queries)):
            ans.append(nextPalindrome(first_palindrome,queries[i]))
        return ans