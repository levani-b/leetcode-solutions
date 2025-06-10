# LeetCode Problem: 3442. Maximum Difference Between Even And Odd Frequency I
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        max_odd = 0
        min_even = float('inf')
        for count in freq.values():
            if count % 2 != 0 and count > max_odd:
                max_odd = count
            elif count % 2 == 0 and count < min_even:
                min_even = count
        
        if max_odd == 0 or min_even == float('inf'):
            return 0
        else:
            return max_odd - min_even