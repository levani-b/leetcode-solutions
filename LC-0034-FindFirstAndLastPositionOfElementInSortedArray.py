# LeetCode Problem: 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(nums) - 1

        found = False
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                found = True
                break
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        if not found:
            return [-1, -1]

        start = end = mid

        while start > 0 and nums[start - 1] == target:
            start -= 1
        
        while end < len(nums) - 1 and nums[end + 1] == target:
            end += 1
        
        return [start, end]
