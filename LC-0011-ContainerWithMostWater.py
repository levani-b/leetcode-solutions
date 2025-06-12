# LeetCode Problem: 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1

        while l != r:
            min_height = min(height[l], height[r])
            length = r - l
            area = length * min_height
            res = max(area, res)
            if height[l] > height[r] or height[l] == height[r]:
                r -= 1
            else:
                l += 1
            
        return res