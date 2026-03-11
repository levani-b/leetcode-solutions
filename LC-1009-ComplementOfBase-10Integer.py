# LeetCode Problem: 1009. Complement of Base 10 Integer
# https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n_binary = format(n, 'b')
        res = ''
        for char in n_binary:
            if char == '0':
                res += '1'
            else:
                res += '0'
        
        return int(res, 2)