class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)


        for word in strs:
            count = [0] * 26
            
            for char in word:
                count[ord(char) - ord("a")] += 1

            result[tuple(count)].append(word)
                

            
        
        answer = []

        for dicts in result.keys():
            answer.append(result[dicts])

        return answer

                
        