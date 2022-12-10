#combining binary search with a bit of data structure
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.records = defaultdict(list)
        pass
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        left,right = 0, len(self.records[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.records[key][mid][0] >= timestamp:
                right = mid - 1
            elif self.records[key][mid][0] < timestamp:
                left = mid + 1 
        self.records[key].insert(left, [timestamp,value])
        pass
        

    def get(self, key: str, timestamp: int) -> str:
        left,right = 0,len(self.records[key]) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            if self.records[key][mid][0] > timestamp:
                right = mid - 1
            if self.records[key][mid][0] <= timestamp:
                left = mid + 1
                res = self.records[key][mid][1]
        return res
        pass
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)x