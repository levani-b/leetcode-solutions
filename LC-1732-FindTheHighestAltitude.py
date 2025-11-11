# LeetCode Problem: 1732. Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        curr_alt = 0
        for alt in gain:
            curr_alt += alt
            if curr_alt > max_alt:
                max_alt = curr_alt        
        return max_alt