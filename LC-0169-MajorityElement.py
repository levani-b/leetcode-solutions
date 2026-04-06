# LeetCode Problem: 169. Majority Element
# https://leetcode.com/problems/majority-element/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            
            if candidate == num:
                count += 1
            else:
                count -= 1
            
        return candidate

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