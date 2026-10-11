class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(self.minimum, val)
        print(self.minimum)
        self.minimums.append(self.minimum)


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.minimums:
            self.minimums.pop()
            self.minimum = self.minimums[-1] if self.minimums else float('inf')
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minimums:
            return self.minimums[-1]
        else: return
            

        
