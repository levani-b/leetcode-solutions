# LeetCode Problem: 334. Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False