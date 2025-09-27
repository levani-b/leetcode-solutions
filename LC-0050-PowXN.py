# LeetCode Problem: 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        half = self.myPow(x, n // 2)
        
        if n % 2 == 0:
            return half * half
        else:
            return x * half * half