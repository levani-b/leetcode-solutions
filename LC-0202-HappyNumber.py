# LeetCode Problem: 202. Happy Number
# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum_of_squares(num):
            total = 0
            while num > 0:
                digit = num % 10
                num //= 10
                total += digit ** 2
            return total
        
        seen = {}

        while n != 1 and n not in seen:
            seen[n] = 1
            n = get_sum_of_squares(n)
        
        return n == 1