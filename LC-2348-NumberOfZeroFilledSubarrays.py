# LeetCode Problem: 2348. Number Of Zero Filled Subarrays
# https://leetcode.com/problems/number-of-zero-filled-subarrays/

from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        streak = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1 * streak
                streak += 1
            elif nums[i] != 0:
                streak = 1
        return count