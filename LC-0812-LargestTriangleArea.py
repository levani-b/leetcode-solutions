# LeetCode Problem: 812. Largest Triangle Area
# https://leetcode.com/problems/largest-triangle-area/

from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def triangleArea(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2  
            x3, y3 = p3
            

            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        
        n = len(points)
        max_area = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    area = triangleArea(points[i], points[j], points[k])
                    max_area = max(max_area, area)
        
        return max_area