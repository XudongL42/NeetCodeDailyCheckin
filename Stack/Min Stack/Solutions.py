class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        if not self.stack:
            raise IndexError("Stack is empty.")
        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            raise IndexError("Stack is empty.")
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            raise IndexError("Stack is empty.")
        return self.min_stack[-1]
        
