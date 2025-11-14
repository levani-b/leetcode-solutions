# LeetCode Problem: 1365. How Many Numbers Are Smaller Than The Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])

        result = [0] * len(nums)
        
        for i, (orig_idx, val) in enumerate(sorted_nums):
            if i > 0 and sorted_nums[i][1] == sorted_nums[i-1][1]:
                result[orig_idx] = result[sorted_nums[i-1][0]]
            else:
                result[orig_idx] = i
        
        return result