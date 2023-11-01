class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        children = {}
        h_map = {}
        for i in range(1,len(parents)):
            if parents[i] in children:
                children[parents[i]].append(i)
            else:
                children[parents[i]] = [i]
        print(children)
        def countNode(n):
            print(n)
            if n in h_map:
                return h_map[n]
            if n not in children:
                left,right = 0,0
                parent = len(parents) - 1
                h_map[n] = [left,right,parent]
                return h_map[n]
            left_count = countNode(children[n][0])
            right_count = None
            if len(children[n]) == 2:
                right_count = countNode(children[n][1])
            left = left_count[0] + left_count[1] + 1
            if right_count:
                right = right_count[0] + right_count[1] + 1
            else:
                right = 0
            parent = len(parents) - left - right - 1
            h_map[n] = [left,right,parent]
            return h_map[n]

            
 
        for i in range(0,len(parents)):
            countNode(i)
        
        ans = 0
        highest = 0
        for node,sub_count in h_map.items():
            score = 1
            for count in sub_count:
                if count != 0:
                    score = score * count
            if score == highest:
                ans += 1
            if score > highest:
                highest = score
                ans = 1
        return ans
            
            
