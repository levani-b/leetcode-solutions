# LeetCode Problem: 3541. Find Most Frequent Vowel And Consonant
# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        char_dict = {}
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
                
        max_vowels = 0
        max_consonant = 0
        for item, val in char_dict.items():
            if item in vowels and val > max_vowels:
                max_vowels = val
            elif item not in vowels and val > max_consonant:
                max_consonant = val
        return max_vowels + max_consonant
            