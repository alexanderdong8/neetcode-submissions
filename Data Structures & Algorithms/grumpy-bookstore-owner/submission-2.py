class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        totals = [0]
        for x in range(len(customers)):
            if not grumpy[x]:
                totals.append(totals[-1] + customers[x])
            else:
                totals.append(totals[-1])

        res = 0
        left = 0
        window = 0
        for right in range(len(customers)):

            if right >= minutes:
                window -= customers[left]
                left += 1

            total = (totals[-1] - totals[right+1]) + totals[left] + window
            #total sum - end of window + beginning of window + the value of the window that i calcualted

            res = max(res, total)

        return res
