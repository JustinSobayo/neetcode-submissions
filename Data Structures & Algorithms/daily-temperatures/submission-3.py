class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        output = [0 for num in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            while s and temp > s[-1][1]:
                pastI, pastT = s.pop()
                output[pastI] = i - pastI
            s.append([i,temp])
        return output
             
