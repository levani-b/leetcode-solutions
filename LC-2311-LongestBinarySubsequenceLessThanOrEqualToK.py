# LeetCode Problem: 2311. Longest Binary Subsequence Less Than or Equal to K
# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        current_value = 0
        power_of_2 = 1
        count = 0
        
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                count += 1
            else:
                if current_value + power_of_2 <= k:
                    current_value += power_of_2
                    count += 1

            if power_of_2 <= k:
                power_of_2 *= 2
        
        return count