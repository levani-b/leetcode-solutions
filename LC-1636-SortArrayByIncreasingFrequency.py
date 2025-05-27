# LeetCode Problem: 1636. Sort Array By Increasing Frequency
# https://leetcode.com/problems/sort-array-by-increasing-frequency/

from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        res = []
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        
        nums.sort(key=lambda x: (nums_dict[x], -x))
        return nums