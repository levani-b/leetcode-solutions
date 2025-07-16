# LeetCode Problem: 3201. Find The Maximum Length Of Valid Subsequence I
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        max_len = 1
    
        even_count = 0
        odd_count = 0
        for num in nums:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        alternating = 0
        last_parity = -1
        for num in nums:
            parity = num % 2
            if last_parity == -1 or parity != last_parity:
                alternating += 1
                last_parity = parity
        
        return max(even_count, odd_count, alternating)