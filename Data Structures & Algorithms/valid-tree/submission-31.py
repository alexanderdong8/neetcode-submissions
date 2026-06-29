class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        treeMap = {}
        for x, y in edges:
            if x not in treeMap:
                treeMap[x] = []
            if y not in treeMap:
                treeMap[y] = []
            treeMap[x].append(y)
            treeMap[y].append(x)
            
        seen = set()
        isTree = [True]

        def dfs(node, prevNode):
            if node in seen:
                isTree[0] = False
                return
            seen.add(node)
            for nextNode in treeMap.get(node, []):
                if nextNode != prevNode:
                    dfs(nextNode, node)
            return
        dfs(0, -1)
        return isTree[0] and len(seen) == n