# LeetCode Problem: 1394. Find Lucky Integer in an Array
# https://leetcode.com/problems/find-lucky-integer-in-an-array/

from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        max_lucky = -1
        for num, count in freq.items():
            if num == count and num > max_lucky:
                max_lucky = num
        
        return max_lucky
                