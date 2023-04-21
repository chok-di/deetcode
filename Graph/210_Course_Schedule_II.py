#topological sort

from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = {i:[] for i in range(numCourses)}
        for [a,b] in prerequisites:
            graph[a].append(b)
        
        cycle = set() #visiting
        def dfs(course):
            if course in res:
                return True
            if course in cycle:
                return False
            cycle.add(course)
            for pre in graph[course]:
                if not dfs(pre): return False
            cycle.remove(course)
            res.append(course)
            return True
        for pre in list(graph):
            if not dfs(pre):
                return []
        return res