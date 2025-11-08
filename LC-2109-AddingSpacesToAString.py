# LeetCode Problem: 2109. Adding Spaces to a String
# https://leetcode.com/problems/adding-spaces-to-a-string/

from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        prev = 0

        for space_pos in spaces:
            res.append(s[prev:space_pos])
            prev = space_pos
        
        res.append(s[prev:])

        return ' '.join(res)