# LeetCode Problem: 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/

from typing import List


def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] !=0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1