# LeetCode Problem: 3232. Find If Digit Game Can Be Won
# https://leetcode.com/problems/find-if-digit-game-can-be-won/

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