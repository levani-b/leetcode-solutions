# LeetCode Problem: 304. Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[0])):
                row.append(0)
            self.prefix_sum.append(row)
        
        for r in range(len(matrix)):
            self.prefix_sum[r][0] = matrix[r][0]
            for c in range(1, len(matrix[0])):
                self.prefix_sum[r][c] = self.prefix_sum[r][c-1] + matrix[r][c]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_region = 0
        for row in range(row1, row2 + 1):
            if col1 > 0:
                sum_region += self.prefix_sum[row][col2] - self.prefix_sum[row][col1-1]
            else:
                sum_region += self.prefix_sum[row][col2]
            
        return sum_region
