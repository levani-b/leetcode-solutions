# LeetCode Problem: 1984. Minimum Difference Between Highest and Lowest of K Scores
# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sr_n = sorted(nums)
        min_diff = float('inf')
        
        if len(nums) == 1:
            return 0
        
        for i in range(len(sr_n) - k + 1):
            diff = sr_n[i + k - 1] - sr_n[i]
            min_diff = min(min_diff, diff)

        return min_diff