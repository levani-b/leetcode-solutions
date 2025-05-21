# LeetCode Problem: 1556. Thousand Separator
# https://leetcode.com/problems/thousand-separator/

class Solution:
    def thousandSeparator(self, n: int) -> str:
        digits = '0123456789'
        result = ''
        count = 0
        if n == 0:
            return '0'
        
        while n > 0:
            digit = n % 10
            result = digits[digit] + result
            n = n // 10
            count += 1
            if count % 3 == 0 and n > 0:
                result = '.' + result
        
        return result