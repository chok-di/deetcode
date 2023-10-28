class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        #distance = [[0 for i in range(len(bikes))] for j in range(len(workers))]
        ans = [-1] * len(workers)
        distance = {}
        for i in range(len(workers)):
            for j in range(len(bikes)):
                m_distance = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                if m_distance not in distance :
                    distance[m_distance] = [(i,j)]
                else:
                    distance[m_distance].append((i,j))
        distance = dict(sorted(distance.items()))
        for key,assignments in distance.items():
            for worker,bike in assignments:
                if ans[worker] == -1 and bike not in ans:
                    ans[worker] = bike
        return ans