# LeetCode Problem: 3731. Find Missing Elements
# https://leetcode.com/problems/find-missing-elements/

from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_num = min(nums)
        max_num = max(nums)

        nums = set(nums)

        res = []
        for val in range(min_num, max_num + 1):
            if val not in nums:
                res.append(val)
        return res