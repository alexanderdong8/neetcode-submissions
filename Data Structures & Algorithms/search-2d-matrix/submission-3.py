class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        bottom, top = 0, len(matrix) - 1
        row_mid = 0
        while bottom <= top:
            row_mid = (top + bottom) // 2

            if target < matrix[row_mid][0]:
                top = row_mid - 1
            elif target > matrix[row_mid][-1]:
                bottom = row_mid + 1
            else:
                break

        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            mid = left + ((right-left) // 2)

            if target == matrix[row_mid][mid]:
                return True
            elif target < matrix[row_mid][mid]:
                right = mid - 1
            else:
                left = mid + 1

        return False
            