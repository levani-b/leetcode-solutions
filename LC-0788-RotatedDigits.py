# LeetCode Problem: 788. Rotated Digits
# https://leetcode.com/problems/rotated-digits/

class Solution:
    def rotatedDigits(self, n: int) -> int:
        invalid = {'3', '4', '7'}
        different = {'2', '5', '6', '9'}
        count = 0
        
        str_n = str(n)

        for num in range(1, n + 1):
            str_num = str(num)
            
            has_invalid = False
            for digit in str_num:
                if digit in invalid:
                    has_invalid = True
                    break
            
            if has_invalid:
                continue
            
            has_different = False
            for digit in str_num:
                if digit in different:
                    has_different = True
                    break
            
            if has_different:
                count += 1
        
        return count