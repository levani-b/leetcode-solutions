# LeetCode Problem: 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        sum_nums = sum(nums)
        for i in range(len(nums) - 1, -1, -1):
            res[i] = sum_nums
            sum_nums -= nums[i]
        return res