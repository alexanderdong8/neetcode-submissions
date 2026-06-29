class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = []

        while i < len(word1) and i < len(word2):
            res.append(word1[i])
            res.append(word2[i])
            i += 1
        
        if len(word1) > len(word2):
            res.extend(word1[len(word2):])

        if len(word2) > len(word1):
            res.extend(word2[len(word1):])

        return "".join(res)