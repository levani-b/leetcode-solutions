# LeetCode Problem: 3330. Find the Original Typed String I
# https://leetcode.com/problems/find-the-original-typed-string-i/

class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = len(word)

        for i in range(1, len(word)):
            if word[i] != word[i-1]:
                count -=1
        return count
