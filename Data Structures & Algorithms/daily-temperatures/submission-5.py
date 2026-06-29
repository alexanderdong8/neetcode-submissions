class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)

        for index in range(len(temperatures)-2, -1, -1):
            back = 1
            while temperatures[index + back] <= temperatures[index]:
                if ans[index + back] == 0:
                    back = 0
                    break
                back += ans[index + back]
            ans[index] = back

        return ans