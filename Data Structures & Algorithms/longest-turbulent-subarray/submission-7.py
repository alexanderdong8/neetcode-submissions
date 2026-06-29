class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        state = "none"
        res = 1
        chainLen = 1
        for x in range(len(arr)-1):
            if state == "none":
                if arr[x] < arr[x+1]:
                    state = "greater"
                    chainLen += 1
                if arr[x] > arr[x+1]:
                    state = "less"
                    chainLen += 1

            elif state == "greater":
                if arr[x] > arr[x+1]:
                    state = "less"
                    chainLen += 1
                elif arr[x] < arr[x+1]:
                    chainLen = 2
                    state = "greater"
                else:
                    chainLen = 1
                    state = "none"

            elif state == "less":
                if arr[x] < arr[x+1]:
                    state = "greater"
                    chainLen += 1
                elif arr[x] > arr[x+1]:
                    chainLen = 2
                    state = "less"
                else:
                    chainLen = 1
                    state = "none"
                
            res = max(res, chainLen)

        return res