# LeetCode Problem: 3727. Maximum Alternating Sum of Squares
# https://leetcode.com/problems/maximum-alternating-sum-of-squares/

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squared_nums = []
        for num in nums:
            squared_nums.append(num ** 2)
        
        sorted_squared = sorted(squared_nums)
        mid_idx = len(sorted_squared) // 2
        
        return sum(sorted_squared) - 2 * sum(sorted_squared[:mid_idx])