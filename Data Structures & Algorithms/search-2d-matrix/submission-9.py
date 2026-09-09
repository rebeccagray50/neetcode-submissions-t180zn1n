class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outerRow, outerCol = len(matrix), len(matrix[0])

        l, r = 0, outerRow*outerCol - 1
        while l <= r: 
            mid = l + (r-l) // 2
            row, col = mid // outerCol, mid % outerCol
            if target > matrix[row][col]: 
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else: 
                return True
        return False 

            

        