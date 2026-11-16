# LeetCode Problem: 389. Find the Difference
# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        for char in t:
            if char not in freq:
                return char
            elif char in freq and freq[char] > 0:
                freq[char] -= 1
            elif char in freq and freq[char] == 0:
                return char
        
