# LeetCode Problem: 3622. Check Divisibility by Digit Sum and Product
# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum_of_digits = 0
        product_of_digits = 1

        for char in str(n):
            sum_of_digits += int(char)
            product_of_digits *= int(char)
        
        if n % (sum_of_digits + product_of_digits) == 0:
            return True
        return False