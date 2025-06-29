# LeetCode Problem: 495. Teemo Attacking
# https://leetcode.com/problems/teemo-attacking/

from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0

        total = 0
        for i in range(len(timeSeries) - 1):
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
        return total + duration
