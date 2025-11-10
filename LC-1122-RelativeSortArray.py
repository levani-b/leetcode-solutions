# LeetCode Problem: 1122. Relative Sort Array
# https://leetcode.com/problems/relative-sort-array/

from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_set = set(arr2)
        freq = {}
        for num in arr1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        res = []
        for num in arr2:
            res += [num] * freq[num]
        
        leftovers = []
        for num, count in freq.items():
            if num not in arr2_set:
                leftovers += [num] * count
        
        return res + sorted(leftovers)