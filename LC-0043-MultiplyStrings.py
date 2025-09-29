# LeetCode Problem: 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 =='0':
            return "0"
        
        def convert_string(num):
            result = 0
            for char in num:
                digit = ord(char) - ord('0')
                result = result * 10 + digit
            return result
        
        num1_int = convert_string(num1)
        num2_int = convert_string(num2)
        multiply = num1_int * num2_int

        res = ''
        while multiply > 0: 
            digit = multiply % 10
            multiply //= 10
            char = chr(digit + ord('0'))
            res = char + res
        
        return res