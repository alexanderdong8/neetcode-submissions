class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        for x in s:
            map1[x] = map1.get(x,0) + 1
        map2 = {}
        for x in t:
            map2[x] = map2.get(x, 0) + 1

        return map1 == map2

        

        