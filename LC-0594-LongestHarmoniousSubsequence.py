# LeetCode Problem: 594. Longest Harmonious Subsequence
# https://leetcode.com/problems/longest-harmonious-subsequence/

from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        j = 0
        maxLength = 0

        for i in range(len(nums)):
            while nums[i] - nums[j] > 1:
                j += 1
            if nums[i] - nums[j] == 1:
                maxLength = max(maxLength, i - j + 1)
        return maxLength
