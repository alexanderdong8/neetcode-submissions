class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}
        s_count = [Counter(s) for s in strs]
        def dfs(index, m_count, n_count):
            if index >= len(strs):
                return 0

            if (index, m_count, n_count) in cache:
                return cache[(index, m_count, n_count)]
                
            if s_count[index]["0"] > m_count or s_count[index]["1"] > n_count:
                cache[(index, m_count, n_count)] = dfs(index+1, m_count, n_count)
                return cache[(index, m_count, n_count)]
            else:
                skip = dfs(index+1, m_count, n_count)
                take = dfs(index+1, m_count - s_count[index]["0"], n_count-s_count[index]["1"])
                cache[(index, m_count, n_count)] = max(skip, take+1)
                return cache[(index, m_count, n_count)]

        res = dfs(0, m, n)
        return res
