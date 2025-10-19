# LeetCode Problem: 2264. Largest 3-Same-Digit Number in String
# https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ''
        max_n = -1
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                digit = ord(num[i]) - ord('0')
                if digit > max_n:
                    max_n = digit
                    res = num[i:i+3]
        return res
