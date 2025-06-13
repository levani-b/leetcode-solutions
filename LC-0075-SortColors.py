# LeetCode Problem: 75. Sort Colors
# https://leetcode.com/problems/sort-colors/

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1


# class Solution:
#     def sortColors(nums: List[int]) -> None:
#             """
#             Do not return anything, modify nums in-place instead.
#             """
#             red = 0
#             white = 0
#             blue = 0
#             for num in nums:
#                 if num == 0:
#                     red+=1
#                 elif num == 1:
#                     white += 1
#                 else:
#                     blue += 1
#             for i in range(len(nums)):
#                 if red >0:
#                     nums[i] = 0
#                     red -= 1
#                 elif white >0:
#                     nums[i] = 1
#                     white -= 1
#                 else:
#                     nums[i] = 2