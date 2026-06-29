class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        edgeMap = {}
        seen = set()
        def dfs(node, prevNode):
            if node in seen:
                return True
            seen.add(node)
            print(seen)
            for nextNode in edgeMap[node]:
                print(nextNode, edgeMap)
                if nextNode != prevNode:
                    if dfs(nextNode, node):
                        return True
            
            return False



        for x, y in edges:
            if x not in edgeMap:
                edgeMap[x] = []
            if y not in edgeMap:
                edgeMap[y] = []
            edgeMap[x].append(y)
            edgeMap[y].append(x)
            seen = set()

            if dfs(x, -1):
                return [x, y]
        return []

            