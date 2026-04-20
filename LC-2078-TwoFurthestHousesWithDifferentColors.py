# LeetCode Problem: 2078. Two Furthest Houses With Different Colors
# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        distance = 0
        start = 0
        while start < len(colors):
            if colors[start] != colors[-1]:
                distance = abs(len(colors) -1 - start)
                break
            start += 1
        
        end = len(colors) - 1

        while end > 0:
            if colors[end] != colors[0]:
                distance = max(distance, end)
                break
            end -= 1
        
        return distance
            