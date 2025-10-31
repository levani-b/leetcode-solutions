# LeetCode Problem: 3289. The Two Sneaky Numbers Of Digitville
# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        seen = set()

        for num in nums:
            if num in seen:
                res.append(num)
            else:
                seen.add(num)
        
        return res