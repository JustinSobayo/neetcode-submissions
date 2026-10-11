class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #what i am going to do is binary search 
        #find the target
        #if the current mid is less than target
        #search right
        #else
        #search left
        #keep cutting array in half
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            print(f"{r} - {l} = {mid}")
            if nums[mid] == target:
                return mid
            if nums[r] == target:
                return r
            if nums[l] == target:
                return l
            if target < nums[mid]:
                r = mid
                l +=1
            else:
                l = mid
                r -=1
                print(r)
        return -1

        