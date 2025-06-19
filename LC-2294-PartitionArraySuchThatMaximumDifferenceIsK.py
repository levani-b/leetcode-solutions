# LeetCode Problem: 2294. Partition Array Such That Maximum Difference Is K
# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        min_val = nums[0]
        for i in range(len(nums)):
            if nums[i] - min_val > k:
                count += 1
                min_val = nums[i]
        return count + 1