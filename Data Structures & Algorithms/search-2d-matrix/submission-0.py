class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom = 0
        top = len(matrix) - 1

        while bottom <= top:
            mid = bottom + ((top - bottom) // 2)

            if target < matrix[mid][0]:
                top = mid - 1
            elif target > matrix[mid][-1]:
                bottom = mid + 1
            else:
                break;

        if bottom > top:
            return False;

        row = matrix[bottom + ((top - bottom) // 2)]
        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            if (target < row[mid]):
                right = mid - 1
            elif (target > row[mid]):
                left = mid + 1
            else:
                return True
                
        return False
            
            