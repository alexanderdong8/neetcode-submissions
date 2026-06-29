class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}
        for x, y in prerequisites:
            if x not in preMap:
                preMap[x] = []
            preMap[x].append(y)
        visited = set()
        seen = set()
        hasCycle = [False]
        res = []
        def dfs(node):
            if node in seen:
                hasCycle[0] = True
                return
            if node in visited:
                return

            seen.add(node)
            print(node)
            for prereq in preMap.get(node, []):
                dfs(prereq)

            seen.remove(node)
            visited.add(node)
            res.append(node)


        for x in range(numCourses):
            if x not in visited:
                dfs(x) 

        if hasCycle[0]:
            return []
        else:
            return res

        