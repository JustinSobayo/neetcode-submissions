class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(self.minimums[-1] if self.minimums else val, val)
        self.minimums.append(val)


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.minimums:
            self.minimums.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums[-1]
            

        
