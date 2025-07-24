# LeetCode Problem: 1417. Reformat The String
# https://leetcode.com/problems/reformat-the-string/

class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []
        
        for char in s:
            if char.isalpha():
                letters.append(char)
            else:
                digits.append(char)
        
        if abs(len(letters) - len(digits)) > 1:
            return ""
        
        if len(letters) > len(digits):
            first, second = letters, digits
        else:
            first, second = digits, letters
        
        result = []
        for i in range(len(s)):
            if i % 2 == 0:
                if first:
                    result.append(first.pop())
            else:
                if second:
                    result.append(second.pop())
        
        return ''.join(result)