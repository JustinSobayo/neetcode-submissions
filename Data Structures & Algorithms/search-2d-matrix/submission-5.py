class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0]) - 1
        larrI = 0
        rarrI = len(matrix) - 1
        midarrI = (larrI + rarrI) // 2
        #while target is not in the mid's array
        #search for the correct mid array
        while larrI <= rarrI:
            print(matrix[midarrI][l])
            if target < matrix[midarrI][l]:
                rarrI = midarrI - 1
                midarrI = (larrI + rarrI) // 2
            elif target > matrix[midarrI][r]:
                print(matrix[midarrI][r])
                larrI = midarrI + 1
                midarrI = (larrI + rarrI) // 2
            else:
                break
        while l <= r:
            mid = (l + r)//2
            if matrix[midarrI][mid] == target:
                return True
            elif matrix[midarrI][mid] > target:
                r = mid - 1
                mid = (l + r)//2
            elif matrix[midarrI][mid] < target:
                l = mid + 1
                mid = (l + r)//2
        return False
            
        
        #once we break out of this, we know that target is
        #inside of the mid array now OR the pointers crossed or equal eachother 
        #we do binary search on the mid array in order to find the target