# LeetCode Problem: 28. Find The Index Of The First Occurrence In A String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0
        n = len(needle)
        occurrence = -1
        for i in range(len(haystack) - n + 1):
            if haystack[i:i + n] == needle:
                occurrence = i
                return occurrence
        
        return occurrence