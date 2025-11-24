# LeetCode Problem: 1018. Binary Prefix Divisible By 5
# https://leetcode.com/problems/binary-prefix-divisible-by-5/

from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        n = len(nums) - 1
        base10 = 0
        for i in range(len(nums)):
            base10 += nums[i] * (2**n)
            res.append(base10 % 5 == 0)
            n -= 1
        return res