# LeetCode Problem: 717. 1-bit and 2-bit Characters
# https://leetcode.com/problems/1-bit-and-2-bit-characters/

from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        
        return i == len(bits) - 1