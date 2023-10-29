class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        sessions  = []
        global shortest
        shortest = float('inf')

        #store all maximized session as tuple in sessions
        def dfs(i,sessions):
            global shortest
            if len(sessions) >= shortest:
                return
            if i == len(tasks):
                shortest = min(shortest,len(sessions))
                return
            for j in range(len(sessions)):
                if sum(sessions[j]) + tasks[i] <= sessionTime:
                    sessions[j].append(tasks[i])
                    dfs(i+1,sessions)
                    sessions[j].pop()
            sessions.append([tasks[i]])
            dfs(i+1,sessions)
            sessions.pop()
        dfs(0,[])
        return shortest

        