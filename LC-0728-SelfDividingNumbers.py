# LeetCode Problem: 728. Self Dividing Numbers
# https://leetcode.com/problems/self-dividing-numbers/

from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(num):
            original = num
            while num > 0:
                digit = num % 10
                if digit == 0 or original % digit != 0:
                    return False
                num //= 10
            return True
        
        res = []
        for num in range(left, right + 1):
            if isSelfDividing(num):
                res.append(num)
        
        return res