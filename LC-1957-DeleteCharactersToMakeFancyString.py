# LeetCode Problem: 1957. Delete Characters to Make Fancy String
# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        
        result = []
        
        for char in s:
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                continue
            else:
                result.append(char)
        
        return ''.join(result)