# LeetCode Problem: 387. First Unique Character In A String
# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashT = {}
        for char in s:
            if char in hashT:
                hashT[char] += 1
            else:
                hashT[char] = 1
        
        for i, char in enumerate(s):
            if hashT[char] == 1:
                return i
        return -1