class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        s_map, t_map = {}, {}
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1

        matches = 0
        res = ""
        reslen = float('inf')
        left = 0
        for index, char in enumerate(s):
            if char in t_map:
                s_map[char] = s_map.get(char, 0) + 1
                if s_map[char] == t_map[char]:
                    matches += 1
            print(s_map, t_map, len(t_map), matches)
            while matches == len(t_map):
                if reslen > (index - left) + 1:
                    res = s[left:index+1]
                    reslen = len(res)
                if s[left] in t_map:
                    s_map[s[left]] -= 1
                    if s_map[s[left]] < t_map[s[left]]:
                        matches -= 1
                left += 1
            
        return res
