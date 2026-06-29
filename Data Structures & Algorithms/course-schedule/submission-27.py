class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        seen = set()
        canFinish = [True]
        prereq_map = {}
        for x, y in prerequisites:
            if x not in prereq_map:
                prereq_map[x] = []
            prereq_map[x].append(y)

        def dfs(node):
            if node in seen:
                canFinish[0] = False
                return
            if node in visited:
                return
            if node not in prereq_map or prereq_map[node] == []:
                return
            seen.add(node)
            for prereq in prereq_map[node]:
                dfs(prereq)
            seen.remove(node)
            visited.add(node)
        
        for x in prereq_map.keys():
            dfs(x)

        return canFinish[0]
