class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        seen = set()
        def dfs(node):
            val = 0
            for newNode in graph[node]:
                if newNode not in seen:
                    seen.add(newNode)
                    val = max(val, dfs(newNode))
                    seen.remove(newNode)

            return val + 1
        res = float('inf')
        height_map = defaultdict(list)
        print(dfs(2))
        print(graph.keys())
        for start in range(n):
            seen.add(start)
            height = dfs(start)
            res = min(res, height)
            height_map[height].append(start)
            seen.remove(start)
        return height_map[res]