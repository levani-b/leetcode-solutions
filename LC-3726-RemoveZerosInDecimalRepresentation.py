# LeetCode Problem: 3726. Remove Zeros In Decimal Representation
# https://leetcode.com/problems/remove-zeros-in-decimal-representation/

class Solution:
    def removeZeros(self, n: int) -> int:
        def int_to_str(number):
            digits = '0123456789'
            result = ''
            while number > 0:
                digit = number % 10
                result = digits[digit] + result
                number //= 10
            return result
        
        s = int_to_str(n)
        result = 0
        for char in s:
            if char != '0':
                digit = ord(char) - ord('0')
                result = result * 10 + digit
        
        return result
