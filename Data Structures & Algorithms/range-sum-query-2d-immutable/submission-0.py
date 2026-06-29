class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = [[0] * (len(matrix[0])+1) for x in range(len(matrix)+1)]

        for x in range(1, len(self.prefix)):
            for y in range(1, len(self.prefix[0])):
                self.prefix[x][y] = self.prefix[x][y-1] + self.prefix[x-1][y] + matrix[x-1][y-1] - self.prefix[x-1][y-1]
        
        '''
        cell[x][y] = prefix[x][y-1] + prefix[x-1][y] + matrix[x][y] - prefix[x-1][y-1]
        '''

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]





        '''
        = prefix[row2+1][col2+1] - prefix[row1][col2+1] - prefix[row2+1][col1] + prefix[row1][col1]
        '''


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)