# LeetCode Problem: 674. Longest Continuous Increasing Subsequence
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

from typing import List


def findLengthOfLCIS(nums: List[int]) -> int:
        max_count = 1
        curr_count = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                curr_count += 1
            else:
                max_count = max(max_count, curr_count)
                curr_count = 1
        return max(max_count, curr_count)