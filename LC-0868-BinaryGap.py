# LeetCode Problem: 868. Binary Gap
# https://leetcode.com/problems/binary-gap/

class Solution:
    def binaryGap(self, n: int) -> int:
        bin_n = f'{n:b}'
        max_gap = 0

        l, r = 0, 1

        while l < len(bin_n) and r < len(bin_n):
            if bin_n[l] == '1':
                if bin_n[r] == '1':
                    max_gap = max(max_gap, r - l)
                    l = r
            else:
                l += 1
            r += 1

        return max_gap
