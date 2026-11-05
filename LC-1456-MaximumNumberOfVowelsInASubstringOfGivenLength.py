# LeetCode Problem: 1456. Maximum Number of Vowels in a Substring Of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_vowels = 0
        for char in s[:k]:
            if char in vowels:
               max_vowels += 1
        curr_vowels = max_vowels
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                curr_vowels -= 1
            
            if s[i] in vowels:
                curr_vowels += 1

            max_vowels = max(curr_vowels, max_vowels)
        
        return max_vowels
