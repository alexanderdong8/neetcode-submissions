class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''
        either multiple values will be in the same triplet but the condition is that they must be alrger than what they are being compared too, or we have 3 separate cases where we have what we want. 
        '''
        res = set()
        for i, j, k in triplets:
            if i > target[0] or j > target[1] or k > target[2]:
                continue

            if i == target[0]:
                res.add(0)

            if j == target[1]:
                res.add(1)

            if k == target[2]:
                res.add(2)

            if len(res) == 3:
                return True

        return False