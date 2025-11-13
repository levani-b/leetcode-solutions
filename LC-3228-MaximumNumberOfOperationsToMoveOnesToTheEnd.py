# LeetCode Problem: 3228. Maximum Number of Operations to Move Ones to the End
# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

class Solution:
    def maxOperations(self, s: str) -> int:
        counted_ones = 0
        operations = 0
        for i in range(len(s)):
            if s[i] == '1':
                counted_ones += 1
            elif s[i] == '0' and i > 0 and s[i-1] == '1':
                operations += counted_ones
        
        return operations 