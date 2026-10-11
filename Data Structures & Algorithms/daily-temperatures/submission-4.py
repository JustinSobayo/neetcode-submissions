class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0 for temper in temperatures]
        #going to store [index, temp] at every index
        #go over every temperature and index in temperatures
        #add every temperature to the stack that we are on
        #if the temperature that we are on is greater than
        #all elements of the stack:top down, that means we need to
        # subtract the index from the bigger temperature from the smaller temperature
        #the bigger temperature would be the temperature that we are currently on in the iteration
        #the smaller temperature is the temperature at the top of the stack
        for i,t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                topI, topT = stack.pop()
                output[topI] = i - topI
            stack.append([i,t])
        return output

