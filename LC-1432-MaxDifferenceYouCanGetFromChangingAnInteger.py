# LeetCode Problem: 1432. Max Difference You Can Get From Changing an Integer
# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

class Solution:
    def maxDiff(self, num: int) -> int:
        s_num = str(num)

        max_num = s_num
        for digit in s_num:
            if digit != '9':
                max_num = s_num.replace(digit, '9')
                break
            
        min_num = s_num
        if s_num[0] != '1':
            min_num = s_num.replace(s_num[0], '1')
        else:
            for digit in s_num[1:]:
                if digit != '0' and digit != '1':
                    min_num = s_num.replace(digit, '0')
                    break
        
        return int(max_num) - int(min_num)