class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        target_positions = [(position[i], speed[i]) for i in range(len(position))]
        target_positions.sort(key = lambda x: x[0])
        stack = []
        print(target_positions)
        for i in range(len(target_positions) - 1, -1, -1):
            print(stack)
            rate = (target - target_positions[i][0]) / target_positions[i][1]
            stack.append(rate)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)