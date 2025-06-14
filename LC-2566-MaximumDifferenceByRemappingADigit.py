# LeetCode Problem: 2566. Maximum Difference by Remapping a Digit
# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

class Solution:
    def minMaxDifference(self, num: int) -> int:
        s_num = str(num)
        
        max_digit = None
        for char in s_num:
            if char != '9':
                max_digit = char
                break
        if max_digit:
            max_num = int(s_num.replace(max_digit, '9'))
        else:
            max_num = num
        
        min_digit = None
        for char in s_num:
            if char != '0':
                min_digit = char
                break
        if min_digit:
            min_num = int(s_num.replace(min_digit, '0'))
        else:
            min_num = num
        
        return max_num - min_num
