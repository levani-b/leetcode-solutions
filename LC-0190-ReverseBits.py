# LeetCode Problem: 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        n_2bit = f"{n:032b}"
        reversed_bits = n_2bit[::-1]
        reversed_num = int(reversed_bits, 2)
        return reversed_num

