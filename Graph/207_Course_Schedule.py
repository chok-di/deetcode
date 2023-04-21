from collections import defaultdict

## fast solution: reassign graph[key] when you know #key class can be finished
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for [a,b] in prerequisites:
            graph[a].append(b)

        visited = set()

        def dfs(key):
            if key in visited:
                return False
            if graph[key] == []:
                return True

            visited.add(key)
            for i in range (len(graph[key])):
                if not dfs(graph[key][i]): return False
            visited.remove(key)
            graph[key] = []
            return True
                

        for key in list(graph):
            if not dfs(key):
                return False
        return True

## slow solution        

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for [a,b] in prerequisites:
            graph[a].append(b)

        visited = set()

        def findCycle(key):
            if key in visited:
                return True
            visited.add(key)
            for i in range(len(graph[key])):
                if findCycle(graph[key][i]):
                    visited.remove(key)
                    return True
            visited.remove(key)
            return False


        for key in list(graph):
            if findCycle(key):
                return False
        return True