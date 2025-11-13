# LeetCode Problem: 848. Shifting Letters
# https://leetcode.com/problems/shifting-letters/

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        reversed_pref_sum = [0] * len(shifts)
        pref_sum = 0
        for i in range(len(shifts)-1, -1, -1):
            pref_sum += shifts[i]
            reversed_pref_sum[i] += pref_sum

        res = ''
        for i in range(len(s)):
            char_code = ord(s[i]) - ord('a')
            shift = reversed_pref_sum[i] % 26
            new_char_code = (char_code + shift) % 26
            res += chr(new_char_code + ord('a'))
        
        return res