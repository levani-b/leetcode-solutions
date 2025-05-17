# LeetCode Problem: 75. Sort Colors
# https://leetcode.com/problems/sort-colors/

from typing import List


def sortColors(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        for num in nums:
            if num == 0:
                red+=1
            elif num == 1:
                white += 1
            else:
                blue += 1
        for i in range(len(nums)):
            if red >0:
                nums[i] = 0
                red -= 1
            elif white >0:
                nums[i] = 1
                white -= 1
            else:
                nums[i] = 2