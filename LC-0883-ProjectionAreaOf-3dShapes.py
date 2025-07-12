# LeetCode Problem: 883. Projection Area of 3D Shapes
# https://leetcode.com/problems/projection-area-of-3d-shapes/

from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        xy_area = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    xy_area += 1
        
        yz_area = 0
        for i in range(n):
            max_height_in_row = max(grid[i])
            yz_area += max_height_in_row
        
        zx_area = 0
        for j in range(n):
            max_height_in_col = max(grid[i][j] for i in range(n))
            zx_area += max_height_in_col
        
        return xy_area + yz_area + zx_area