class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #phone:
        p = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        if not digits:
            return []
        ans = [""]
        for i in range(len(digits)):
            new_ans = []
            while ans:
                s = ans.pop()
                for c in p[digits[i]]:
                    new = s + c
                    new_ans.append(new)
            ans = new_ans
        return ans