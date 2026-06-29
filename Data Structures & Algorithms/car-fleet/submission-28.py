class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [[pos, speed] for pos, speed in zip(position, speed)]
        pos_speed.sort(key=lambda x: x[0])
        print(pos_speed)
        times = [(target - pos) / speed for pos, speed in pos_speed]

        stack = []
        print(times)
        for time in times:
            if not stack:
                stack.append(time)
            else:
                while stack and stack[-1] <= time:
                    stack.pop()
                stack.append(time)

        return len(stack)