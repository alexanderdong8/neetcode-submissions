from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        seen = set(["0000"])
        queue = deque([("0000", 0)])

        while queue:

            code, turns = queue.popleft()

            if code in deadends:
                continue
            if code == target:
                return turns
            for x in range(len(code)):
                nextDigit = (int(code[x]) + 1) % 10
                nextCode = code[:x] + str(nextDigit) + code[x+1:]
                if nextCode not in seen:
                    seen.add(nextCode)
                    queue.append((nextCode, turns+1))

                nextDigit = (int(code[x]) - 1) % 10
                nextCode = code[:x] + str(nextDigit) + code[x+1:]
                if nextCode not in seen:
                    seen.add(nextCode)
                    queue.append((nextCode, turns+1))

        return -1


