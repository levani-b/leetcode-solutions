# LeetCode Problem: 762. Prime Number Of Set Bits In Binary Representation
# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def count_of_one(s):
            c = 0
            for char in s:
                if char == '1':
                    c += 1
        
            return c
        
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        prime_count = 0
        for i in range(left, right + 1):
            bin_number = f"{i:b}"
            if is_prime(count_of_one(bin_number)):
                prime_count += 1

        return prime_count