# LeetCode Problem: 2154. Keep Multiplying Found Values By Two
# https://leetcode.com/problems/keep-multiplying-found-values-by-two/

from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num_set = set(nums)
        while original in nums:
            original *= 2
        return original