# LeetCode Problem: 1295. Find Numbers With Even Number Of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

from typing import List

def findNumbers(self, nums: List[int]) -> int:
    count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            count +=1
    return count 