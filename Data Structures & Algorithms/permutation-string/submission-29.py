class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_arr = [0] * 26
        s2_arr = [0] * 26
        matches = 0
        left = 0
        for i in range(len(s1)):
            s1_arr[ord(s1[i]) - ord('a')] += 1
            s2_arr[ord(s2[i]) - ord('a')] += 1
        
        for index, val in enumerate(s1_arr):
            if s1_arr[index] == s2_arr[index]:
                matches += 1

        if matches == 26:
            return True
        for j in range(len(s1), len(s2)):
            print(s1_arr, s2_arr, matches)

            index = ord(s2[j]) - ord('a')
            s2_arr[index] += 1
            if s2_arr[index] == s1_arr[index]:
                matches += 1
            elif s1_arr[index] + 1 == s2_arr[index]:
                matches -= 1

            index = ord(s2[left]) - ord('a')
            s2_arr[index] -= 1
            if s2_arr[index] == s1_arr[index]:
                matches += 1
            elif s1_arr[index] - 1 == s2_arr[index]:
                matches -= 1
            left += 1

            if matches == 26:
                return True

        return False