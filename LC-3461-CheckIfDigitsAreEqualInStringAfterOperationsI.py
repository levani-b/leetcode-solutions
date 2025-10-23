# LeetCode Problem: 3461. Check If Digits Are Equal In String After Operations I
# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 1:
            if len(s) == 2 and s[0] == s[1]:
                return True
                
            res = ''
            for i in range(len(s) - 1):
                op = (int(s[i]) + int(s[i+1])) % 10
                res += str(op)
            
            s = res
        return False