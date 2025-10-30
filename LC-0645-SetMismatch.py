# LeetCode Problem: 645. Set Mismatch
# https://leetcode.com/problems/set-mismatch/

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = 0
        missing = 0

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        for i in range(1,len(nums) + 1):
            if i not in seen:
                missing = i
                break
        return [duplicate, missing]