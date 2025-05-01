# LeetCode Problem: 268. Missing Number
# https://leetcode.com/problems/missing-number/

from typing import List


def missingNumber(nums: List[int]) -> int:
        hash_table = {}
        for num in nums:
            hash_table[num] = True
        for i in range(len(nums) + 1):
            if i not in hash_table:
                return i
        return -1