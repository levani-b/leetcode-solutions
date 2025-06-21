# LeetCode Problem: 169. Majority Element
# https://leetcode.com/problems/majority-element/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums) // 2
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

            if freq[num] > maj:
                return num