# LeetCode Problem: 2894. Divisible And Non Divisible Sums Difference
# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum1 = 0
        sum2 = 0
        for num in range(1,n+1):
            if num % m != 0:
                sum1 += num
            else:
                sum2 += num
    
        return sum1-sum2