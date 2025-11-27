# LeetCode Problem: 3754. Concatenate Non-Zero Digits and Multiply By Sum I
# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n_str = str(n)
        
        x = ''
        for digit in n_str:
            if digit != '0':
                x += digit
        
        sum_x = 0
        for digit in n_str:
            if digit != '0':
                sum_x += int(digit)
        
        return int(x) * sum_x if x else 0
