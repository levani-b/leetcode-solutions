# LeetCode Problem: 2269. Find the K Beauty of a Number
# https://leetcode.com/problems/find-the-k-beauty-of-a-number/

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        divisors = 0
        num_st = str(num)

        for i in range(len(num_st) - k + 1):
            divisor = int(num_st[i:i+k])
            if divisor != 0 and num % divisor == 0:
                divisors += 1
        
        return divisors
