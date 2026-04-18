# LeetCode Problem: 3783. Mirror Distance Of An Integer
# https://leetcode.com/problems/mirror-distance-of-an-integer/

class Solution:
    def mirrorDistance(self, n: int) -> int:
        if n < 10:
            return 0
            
        n_cp = n
        rev = 0
        while n_cp > 0:
            digit = n_cp % 10
            rev = (rev * 10) + digit
            n_cp //= 10
        
        return abs(n - rev)  