# LeetCode Problem: 1422. Maximum Score After Splitting a String
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        sum_ones = 0
        for char in s:
            if char == "1":
                sum_ones += 1

        max_score = 0
        left_zeros = 0
        right_ones = sum_ones
        for i in range(len(s) - 1):
            if s[i] == "0":
                left_zeros += 1
            else:
                right_ones -= 1
            curr_score = left_zeros + right_ones
            if curr_score > max_score:
                max_score = curr_score
        
        return max_score