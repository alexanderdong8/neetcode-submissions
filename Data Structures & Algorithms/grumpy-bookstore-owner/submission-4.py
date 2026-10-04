class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total = 0
        window = 0

        left = 0
        max_window = 0
        for right in range(len(customers)):
            #you can also just keep track of the largest window and append it to the total
            if not grumpy[right]:
                total += customers[right]
            else:
                window += customers[right]

            if right >= minutes:
                window -= customers[left] if grumpy[left] else 0
                left += 1

            max_window = max(max_window, window)

        return max_window + total