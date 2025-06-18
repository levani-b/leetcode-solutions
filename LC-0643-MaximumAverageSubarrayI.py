# LeetCode Problem: 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        l = 0
        for i in range(k, len(nums)):
            curr_sum = curr_sum + nums[i] - nums[l]
            if curr_sum > max_sum:
                max_sum = curr_sum
            l+=1
        return max_sum / k