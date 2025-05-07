# LeetCode Problem: 1. Two Sum
# https://leetcode.com/problems/two-sum/

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in nums[i+1:]:
                j = nums.index(diff, i+1)
                return [i,j]