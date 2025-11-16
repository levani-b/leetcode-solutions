# LeetCode Problem: 1513. Number of Substrings With Only 1s
# https://leetcode.com/problems/number-of-substrings-with-only-1s/

class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        result = 0
        count = 0  
        
        for char in s:
            if char == '1':
                count += 1
                result = (result + count) % MOD
            else:
                count = 0
        
        return result