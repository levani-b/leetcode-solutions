# LeetCode Problem: 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        map_s = {}
        map_p = {}
        res = []
        window = len(p)

        for char in p:
            if char in map_p:
                map_p[char] += 1
            else:
                map_p[char] = 1
        
        for i in range(window):
            char = s[i]
            map_s[char] = map_s.get(char, 0) + 1
        
        if map_s == map_p:
            res.append(0)
        
        for i in range(window, len(s)):
            new_char = s[i]
            map_s[new_char] = map_s.get(new_char, 0) + 1
            
            
            old_char = s[i - window]
            map_s[old_char] -= 1
            if map_s[old_char] == 0:
                del map_s[old_char]
            
            if map_s == map_p:
                res.append(i - window + 1)
        
        return res