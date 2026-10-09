class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == '+':
                if len(record) >= 2:
                    x = int(record[-1])
                    y = int(record[-2])
                    record.append(x+y)
            elif op == 'C':
                if record:
                    record.pop()
            elif op == 'D':
                if record:
                    num = int(record[-1])
                    num *= 2
                    record.append(num)
            else:
                record.append(int(op))
            print(record)
        return sum(record)


        