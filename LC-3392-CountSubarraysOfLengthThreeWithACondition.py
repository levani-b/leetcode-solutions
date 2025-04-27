# LeetCode Problem: 3392. Count Subarrays Of Length Three With A Condition
# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

from typing import List

def countSubarrays(self, nums: List[int]) -> int:
    n = len(nums)

    count = 0
    for i in range(n-2):
        if nums[i] + nums[i+2] == nums[i+1]/2:
            count += 1
    return count 