# LeetCode Problem: 3432. Maximum Difference Between Adjacent Elements In A Circular Array
# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_so_far = 0
        n = len(nums)
        for i in range(1,n):
            if max_so_far < abs(nums[i] - nums[i-1]):
                max_so_far = abs(nums[i] - nums[i-1])
        
        if abs(nums[n - 1] - nums[0]) > max_so_far:
            max_so_far = abs(nums[n - 1] - nums[0])
        
        return max_so_far