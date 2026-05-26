# LeetCode Problem: 3120. Count The Number Of Special Characters I
# https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word_set = set(word)
        count = 0
        
        for i in range(26):
            lower = chr(ord('a') + i)
            upper = chr(ord('A') + i)
            if lower in word_set and upper in word_set:
                count += 1
        
        return count