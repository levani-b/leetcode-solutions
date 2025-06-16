# LeetCode Problem: 2016. Maximum Difference Between Increasing Elements
# https://leetcode.com/problems/maximum-difference-between-increasing-elements/

from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        min_so_far = nums[0]

        for i in range(1,len(nums)):
            if min_so_far < nums[i]:
                if nums[i] - min_so_far > max_diff:
                    max_diff = nums[i] - min_so_far

            if nums[i] < min_so_far:
                min_so_far = nums[i]
                
        return max_diff