class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outer = 0 
        found = False
        while found == False: 
            currentRow = matrix[outer]
            l = 0
            r = len(currentRow)-1
            if currentRow[r] < target: 
                outer += 1
                next
            elif currentRow[r] > target: 
                while l < r: 
                    mid = l + ((r - l) // 2)
                    if currentRow[mid] > target: 
                        r = mid
                    elif currentRow[mid] <= target: 
                        l = mid + 1
                return True if (l and currentRow[l-1] == target) else False
            return False
