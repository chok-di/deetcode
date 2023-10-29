class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        b_count = 0
        w_count = 0
        for i in range(0,k):
            if blocks[i] == 'B':
                b_count += 1
            else:
                w_count += 1
        res = w_count
        for i in range(k,len(blocks)):
            print(i,res)
            w_count = w_count - 1 if blocks[i-k] == 'W' else w_count 
            w_count = w_count + 1 if blocks[i] == 'W' else w_count 
            res = min(res,w_count)
        return res

