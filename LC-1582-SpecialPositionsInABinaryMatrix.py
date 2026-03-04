# LeetCode Problem: 1582. Special Positions In A Binary Matrix
# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        rows = len(mat)
        cols = len(mat[0])

        row_count = []
        for i in range(rows):
            count = 0
            for j in range(cols):
                if mat[i][j] == 1:
                    count += 1
            row_count.append(count)
        
        col_count = []
        for j in range(cols):
            count = 0
            for i in range(rows):
                if mat[i][j] == 1:
                    count += 1
            col_count.append(count)
        
        special_count = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    if row_count[i] == 1 and col_count[j] == 1:
                        special_count += 1
        
        return special_count