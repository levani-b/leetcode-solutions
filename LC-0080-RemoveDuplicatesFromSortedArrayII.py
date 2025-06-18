# LeetCode Problem: 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 2
        for r in range(2, len(nums)):
            if nums[r] != nums[l-2]:
                nums[l] = nums[r]
                l += 1
        return l