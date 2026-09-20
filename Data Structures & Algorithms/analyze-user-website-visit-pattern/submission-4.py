class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        '''
        Input: username = 
        ["bob","bob","bob","alice","alice","alice","alice","charlie","charlie","charlie"] 
        timestamp = [1,2,3,4,5,6,7,8,9,10], 
        website = 
        ["home","about","career","home","cart","maps","home","home","about","career"]

        Output: ["home","about","career"]
        '''
        input = []
        for x in range(len(username)):
            input.append((username[x], timestamp[x], website[x]))

        input.sort(key=lambda x: x[1])

        sequences = defaultdict(list)
        for x in range(len(username)):
            sequences[input[x][0]].append(input[x][2])

        combo_count = defaultdict(int)

        for name in sequences.keys():
            arr = sequences[name]
            seen = set()
            if len(arr) < 3:
                continue
            for i in range(len(arr)-2):
                for j in range(i+1, len(arr)-1):
                    for k in range(j+1, len(arr)):
                        combo = (arr[i], arr[j], arr[k])
                        if combo not in seen:
                            seen.add(combo)
                            combo_count[combo] += 1
            # for x in range(len(arr) - 2):
            #     if len(arr) < 3:
            #         break
            #     combo = (arr[x], arr[x+1], arr[x+2])
            #     if combo not in seen:
            #         seen.add(combo)
            #         combo_count[combo] += 1

        res = []
        for combo, count in combo_count.items():
            res.append((count, combo))

        res.sort(key=lambda x: (-x[0], x[1]))
        print(res)
        return list(res[0][1])

                
                
                
        