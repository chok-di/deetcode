class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals or newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        i = 0
        #skip intervals finished before newInterval
        #at the end of this loop,new interval start before ith interval finishes 
        while intervals[i][1] < newInterval[0]:
            i += 1
        #no overlapping
        if intervals[i][0] > newInterval[1]:
            intervals.insert(i,newInterval)
            return intervals
        #overlapping
        intervals[i][0] = min(newInterval[0],intervals[i][0])
        intervals[i][1] = max(newInterval[1],intervals[i][1])
        while i < len(intervals) - 1 and intervals[i][1] >= intervals[i+1][0]:
            intervals[i][1] = max(newInterval[1],intervals[i+1][1])
            intervals.pop(i+1)
        return intervals