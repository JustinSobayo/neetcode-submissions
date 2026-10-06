class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        twos = 0
        ones = 0
        zeros = 0
        for num in nums:
            if num == 2:
                twos +=1
                print(twos)
            elif num == 1:
                ones += 1
                print(ones)
            elif num == 0:
                zeros +=1
                print(zeros)
        for i in range(len(nums)):
            if zeros != 0:
                nums[i] = 0
                zeros -= 1
                print(zeros)
            elif ones != 0:
                nums[i] = 1
                ones -=1
                print(ones)
            elif twos != 0:
                nums[i] = 2
                twos -= 1
                print(twos)