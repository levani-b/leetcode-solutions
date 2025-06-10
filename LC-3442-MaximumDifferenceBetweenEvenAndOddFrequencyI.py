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

        freq_odd, freq_even = [],[]
        for count in freq.values():
            if count % 2 != 0:
                freq_odd.append(count)
            else:
                freq_even.append(count)
        
        if len(freq_odd) == 0 or len(freq_even) == 0:
            return 0

        max_diff = freq_odd[0] - freq_even[0]

        for odd in freq_odd:
            for even in freq_even:
                if odd - even > max_diff:
                    max_diff = odd - even

        return max_diff
        