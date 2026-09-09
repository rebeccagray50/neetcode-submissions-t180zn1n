class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outerRow, outerCol = len(matrix), len(matrix[0])

        row, col = 0, outerRow*outerCol - 1
        while l <= r: 
            mid = l + (r-l) // 2
            
        