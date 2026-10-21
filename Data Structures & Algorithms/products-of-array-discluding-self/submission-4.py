class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        output = []
        for i in range(len(nums)):
            output.append(pre)
            pre *=nums[i]
            post = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= post
            post *= nums[j]
        return output

        