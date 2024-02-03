class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,cols=len(matrix)+1, len(matrix[0])+1
        self.prefix_matrix=[[0]*cols for _ in range(rows)]
        for r in range(len(matrix)):
            prefix=0
            for c in range(len(matrix[0])):
                prefix+=matrix[r][c]
                top=self.prefix_matrix[r][c+1]
                self.prefix_matrix[r+1][c+1]=prefix+top

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2=row1+1, col1+1, row2+1, col2+1
        bottom=self.prefix_matrix[row2][col2]
        top=self.prefix_matrix[row1-1][col2]
        left=self.prefix_matrix[row2][col1-1]
        top_left=self.prefix_matrix[row1-1][col1-1]
        return bottom - left - top + top_left

        




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)