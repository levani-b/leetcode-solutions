# LeetCode Problem: 3151. Special Array
# https://leetcode.com/problems/special-array/

from typing import List


def canAliceWin(self, nums: List[int]) -> bool:
        sum1 = 0
        sum2 = 0
        for num in nums:
            if num < 10:
                sum1+= num
            else:
                sum2 += num
        return sum1 != sum2