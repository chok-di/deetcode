class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        def make_move(start,end):
            if (start,end) in dp:
                return dp[(start,end)]
            if start == end:
                return nums[start]
            option1 =  nums[start] - make_move(start+1,end)
            option2 = nums[end] - make_move(start,end - 1)
            max_diff = max(option1,option2)
            dp[(start,end)] = max_diff
            return max_diff
        return make_move(0,len(nums) - 1) >= 0