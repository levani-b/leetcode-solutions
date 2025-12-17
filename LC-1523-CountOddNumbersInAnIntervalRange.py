# LeetCode Problem: 1523. Count Odd Numbers in an Interval Range
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = high - low + 1
        num_to_add = 0
        if low % 2 == 1:
            num_to_add = 1
       
        if total % 2 == 1:
            return (total // 2) + num_to_add
        else:
            return total // 2