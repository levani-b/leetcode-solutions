# LeetCode Problem: 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        res = [[1]]
        for _ in range(1, numRows):
            temp = [0] + res[-1] + [0]
            row = []

            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)

        return res
