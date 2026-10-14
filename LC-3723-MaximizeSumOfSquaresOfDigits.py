# LeetCode Problem: 3723. Maximize Sum Of Squares Of Digits
# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

class Solution:
    def maxSumOfSquares(self, num: int, sum_val: int) -> str:
        if sum_val > num * 9 or sum_val == 0:
            return ""
        
        digits = [0] * num
        remaining = sum_val

        for i in range(num):
            digits[i] = min(9, remaining)
            remaining -= digits[i]
        
        return ''.join(map(str, digits))