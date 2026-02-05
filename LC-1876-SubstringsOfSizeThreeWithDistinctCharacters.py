# LeetCode Problem: 1876. Substrings Of Size Three With Distinct Characters
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
        good_substr = 0

        for i in range(len(s) - k + 1):
            if len(set(s[i:i + k])) == 3:
                good_substr += 1
        
        return good_substr