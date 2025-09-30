# LeetCode Problem: 2221. Find Triangular Sum Of An Array
# https://leetcode.com/problems/find-triangular-sum-of-an-array/

from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            for i in range(n-1):
                nums[i] = (nums[i]+nums[i+1]) % 10
            n -= 1

        return nums[0]