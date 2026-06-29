class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = collections.defaultdict(int)
        for c in s1:
            s1_map[c] += 1

        left = 0
        s2_map = collections.defaultdict(int)
        for right in range(len(s2)):
            s2_map[s2[right]] += 1
            if right > len(s1) - 1:
                s2_map[s2[left]] -= 1
                if s2_map[s2[left]] == 0:
                    del s2_map[s2[left]]
                left += 1
            if s1_map == s2_map:
                return True
            print(right, s1_map, s2_map)

        return False
            