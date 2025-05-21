# LeetCode Problem: 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        hi = len(nums) -1

        while low <= hi:
            mid = (low + hi) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                low = mid + 1
            else:
                hi = mid - 1
        return low