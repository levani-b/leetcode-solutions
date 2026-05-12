# LeetCode Problem: 459. Repeated Substring Pattern
# https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for length in range(1, n):
            if n % length == 0:
                pattern = s[:length]
                times = n // length
                if pattern * times == s:
                    return True
        return False