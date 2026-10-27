# LeetCode Problem: 3969. Create Grid With Exactly One Path
# https://leetcode.com/problems/create-grid-with-exactly-one-path/

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        for i in range(m):
            curr_row = ''
            for j in range(n):
                if i == 0 or j == n - 1:
                    curr_row += '.'
                else:
                    curr_row += '#'
            grid.append(curr_row)
        return grid
