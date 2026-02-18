# LeetCode Problem: 693. Binary Number with Alternating Bits
# https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary_str = f'{n:b}'
        for i in range(1,len(binary_str)):
            if binary_str[i] == binary_str[i-1]:
                return False
        
        return True