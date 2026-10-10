class MinStack:

    def __init__(self):
        self.stack = []
        self.small = float('inf')

    def push(self, val: int) -> None:
        self.small = min(self.small, val)
        self.stack.append((val, self.small))

    def pop(self) -> None:
        val, minimum = self.stack.pop()
        if minimum == self.small:
            self.small = self.stack[-1][1] if self.stack else float('inf')

    def top(self) -> int:
        
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

