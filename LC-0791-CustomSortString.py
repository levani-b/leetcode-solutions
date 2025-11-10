# LeetCode Problem: 791. Custom Sort String
# https://leetcode.com/problems/custom-sort-string/

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        res = ''
        for char in order:
            if char in freq:
                res += char * freq[char]
        
        for char, count in freq.items():
            if char not in res:
                res += char * count
        
        return res