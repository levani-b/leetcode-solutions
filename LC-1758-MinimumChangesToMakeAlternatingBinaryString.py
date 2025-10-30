# LeetCode Problem: 1758. Minimum Changes To Make Alternating Binary String
# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution:
    def minOperations(self, s: str) -> int:
        op1 = 0
        op2 = 0
        
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    op1 += 1
                if s[i] != '1':
                    op2 += 1
            else:
                if s[i] != '1':
                    op1 += 1
                if s[i] != '0':
                    op2 += 1
        
        return min(op1, op2)