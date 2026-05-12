# LeetCode Problem: 482. License Key Formatting
# https://leetcode.com/problems/license-key-formatting/

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        first_group_len = len(s) % k

        if first_group_len == 0:
            first_group_len = k
        
        result = s[:first_group_len]

        for i in range(first_group_len, len(s), k):
            result += '-' + s[i:i+k]
        
        return result