class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        supermap = {}

        for word in strs:
            arr = 26 * [0]
            for char in word:
                num = ord(char) - ord("a")
                arr[num] += 1
            
            if tuple(arr) not in supermap:
                supermap[tuple(arr)] = []
            supermap[tuple(arr)].append(word)
                
        return list(supermap.values()) 
