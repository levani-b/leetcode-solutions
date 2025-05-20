# LeetCode Problem: 3550. Smallest Index With Digit Sum Equal To Index
# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sum_of_digits(n):
            n = abs(n)
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total
        
        for i, num in enumerate(nums):
            sum_digits = sum_of_digits(num)
            if i == sum_digits:
                return i
        return -1