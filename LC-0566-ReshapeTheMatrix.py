# LeetCode Problem: 566. Reshape The Matrix
# https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat
        
        res = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(0)
            res.append(row)
        
        for i in range(m):
            for j in range(n):
                index = i * n + j
                r_idx = index // c
                c_idx = index % c
                res[r_idx][c_idx] = mat[i][j]
            
        return res

# class Solution:
#     def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
#         m, n = len(mat), len(mat[0])

#         if m * n != r * c:
#             return mat
        
#         res = []
#         new_row = []

#         for i in range(m):
#             for j in range(n):
#                 new_row.append(mat[i][j])

#                 if len(new_row) == c:
#                     res.append(new_row)
#                     new_row = []
        
#         return res