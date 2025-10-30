# LeetCode Problem: 1897. Redistribute Characters To Make All Strings Equal
# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = {}
        for word in words:
            for char in word:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
        
        n = len(words)
        for count in freq.values():
            if count % n != 0:
                return False
        
        return True