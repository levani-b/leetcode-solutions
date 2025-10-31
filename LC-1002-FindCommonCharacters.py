# LeetCode Problem: 1002. Find Common Characters
# https://leetcode.com/problems/find-common-characters/

from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq = {}
        for char in words[0]:
            if char in min_freq:
                min_freq[char] += 1
            else:
                min_freq[char] = 1
        
        for i in range(1, len(words)):
            curr_freq = {}
            for char in words[i]:
                if char in curr_freq:
                    curr_freq[char] += 1
                else:
                    curr_freq[char] = 1
            
            for char in min_freq:
                if char in curr_freq:
                    min_freq[char] = min(min_freq[char], curr_freq[char])
                else:
                    min_freq[char] = 0
        
        res = []
        for char, count in min_freq.items():
            for _ in range(count):
                res.append(char)
        
        return res