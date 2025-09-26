# LeetCode Problem: 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        temp = x
        result = 0
        while temp > 0:
            remain = temp % 10
            temp //=10
            result = result * 10 + remain
        
        return result == x