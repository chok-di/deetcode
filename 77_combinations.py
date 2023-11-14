class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def fn(c,i):
            if len(c) == k:
                ans.append(c)
                return
            if i > n:
                return
            for index in range(i,n+1):
                new_c = c.copy()
                new_c.append(index)
                fn(new_c,index+1)
        fn([],1)
        return ans