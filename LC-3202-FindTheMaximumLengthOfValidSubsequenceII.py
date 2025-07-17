# LeetCode Problem: 3202. Find the Maximum Length of Valid Subsequence II
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        max_length = 1
        
        for target_sum in range(k):
            dp = [0] * k
            
            for num in nums:
                remainder = num % k
                prev_remainder = (target_sum - remainder) % k
                
                if dp[prev_remainder] > 0:
                    dp[remainder] = max(dp[remainder], dp[prev_remainder] + 1)
                else:
                    dp[remainder] = max(dp[remainder], 1)
                
                max_length = max(max_length, dp[remainder])
        
        return max_length