class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            res = x

            while x != p[x]:
                p[x] = p[p[x]]
                x = p[x]

            return x
        
        def join(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return 0

            if rank[y] > rank[x]:
                p[p1] = p2
            else:
                p[p2] = p1

            return 1
        res = n
        for x, y in edges:
            res -= join(x, y)

        return res


        

            
