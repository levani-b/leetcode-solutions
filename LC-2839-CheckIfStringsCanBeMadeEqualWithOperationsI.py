# LeetCode Problem: 2839. Check if Strings Can be Made Equal With Operations I
# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (sorted(s1[::2]) == sorted(s2[::2]) and
                sorted(s1[1::2]) == sorted(s2[1::2]))