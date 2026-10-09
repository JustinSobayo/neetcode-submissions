class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0 for num in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]:
                stackT, stackInd = stack.pop()
                output[stackInd] = i - stackInd
            stack.append([temp, i])
        return output


             
