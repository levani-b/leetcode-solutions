# LeetCode Problem: 409. Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        length = 0
        has_odd = False 

        for count in freq.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                has_odd =True
        
        if has_odd:
            length += 1
        
        return length