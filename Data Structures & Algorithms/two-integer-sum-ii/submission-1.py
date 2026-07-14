class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        #[1,2,3,4]
#         l
#               r
        while l<r:
            if numbers[l] + numbers[r] > target:
                r -= 1
                continue
            elif numbers[l] + numbers[r] < target:
                l += 1
                continue
            elif numbers[l]+numbers[r] == target:
                return [l+1, r+1]
            

