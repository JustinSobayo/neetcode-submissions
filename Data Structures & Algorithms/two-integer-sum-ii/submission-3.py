class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #there is always 2 numbers that add to target
        l = 0
        r = len(numbers) - 1
        while l < r:
            #if left + right == target:
            #return l, r
            if numbers[l] + numbers[r] == target:
                return [l+ 1, r+ 1]
            #if sum is greater than target: move right pointer down
            #if not move left
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
        
                 
