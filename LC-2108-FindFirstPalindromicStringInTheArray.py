# LeetCode Problem: 2108. Find First Palindromic String in the Array
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(s: str) -> bool:
            left = 0
            right = len(s) - 1
            
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True
        
        for word in words:
            if is_palindrome(word):
                return word
        
        return ""
