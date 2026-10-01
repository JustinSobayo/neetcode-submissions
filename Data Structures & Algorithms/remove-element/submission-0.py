class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valid = len(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                move = nums[i]
                nums.append(move)
                count +=1
        length = valid - count
        for i in range(len(nums)):
            while nums[i] == val:
                nums.pop(i)
                if i >= length:
                    break
            if i>= length:
                break
        return length