# LeetCode Problem: 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros_position = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeros_position.append([i,j])
        
        for pos in zeros_position:
            row, col = pos
            for j in range(len(matrix[row])):
                matrix[row][j] = 0
            
            for i in range(len(matrix)):
                matrix[i][col] = 0
