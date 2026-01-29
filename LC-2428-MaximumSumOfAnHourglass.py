# LeetCode Problem: 2428. Maximum Sum Of An Hourglass
# https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_sum = 0

        for i in range(rows-2):
            for j in range(cols-2):
                hourglass_sum = (
                    grid[i][j] + grid[i][j+1] + grid[i][j+2] +
                    grid[i+1][j+1] + grid[i+2][j+2] + grid[i+2][j+1] + grid[i+2][j]
                )

                max_sum = max(hourglass_sum, max_sum)
        
        return max_sum