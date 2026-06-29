class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for start, end in prerequisites:
            graph[start].append(end)
        hasCycle = False
        seen = set()
        visited = set()
        res = []
        def dfs(node):
            print(node)
            nonlocal hasCycle
            if hasCycle:
                return
            for newNode in graph[node]:
                if newNode in visited:
                    continue
                if newNode not in seen:
                    seen.add(newNode)
                    dfs(newNode)
                    seen.remove(newNode)
                else:
                    hasCycle = True

            
            visited.add(node)
            res.append(node)

        for num in range(numCourses):
            if num not in visited:
                dfs(num)
        
        return [] if hasCycle else res
        